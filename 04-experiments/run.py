#!/usr/bin/env python3
"""Demonstration run for 04-experiments/00-DEMONSTRATION-PREREG.md.

Every number in 01-RESULT.md comes from this script. Nothing is typed by hand.
Constants below are the ones fixed in the pre-registration, committed earlier
and not edited afterwards.
"""
import csv, json, math, sys
import numpy as np

# ---- constants fixed by the pre-registration (do not edit) -------------------
CV_SEED, BOOT_SEED = 20260820, 20260821
N_BOOT, K_FOLDS = 1000, 5
P_T_GRID = [0.02, 0.05, 0.10, 0.20, 0.30, 0.50]
DELTA_LO, DELTA_HI = 0.001, 0.05
OCC_MIN, BRACKET_MAX, B_MIN, PI_MAX = 0.90, 0.25, 0.5, 0.15

# ---- declared feature set S (declared in 00b-DATASET-CHOICE.md before the run)
# census-income.data has no header; positions follow the attribute order in
# census-income.names.
COL = {'education': 4, 'major occupation code': 9, 'class of worker': 1,
       'full or part time employment stat': 15, 'marital stat': 7,
       'citizenship': 35, 'race': 10, 'sex': 12}
S = list(COL)
TARGET_IDX, POS_PREFIX, NCOL = 41, '50000+', 42


def load(path):
    with open(path, newline='') as fh:
        rows = [r for r in csv.reader(fh) if len(r) >= NCOL]
    y = np.array([1 if r[TARGET_IDX].strip().startswith(POS_PREFIX) else 0 for r in rows],
                 dtype=np.int64)
    codes, cards = {}, {}
    for f in S:
        vals = [r[COL[f]].strip() or '__MISSING__' for r in rows]
        uniq = sorted(set(vals))
        idx = {v: i for i, v in enumerate(uniq)}
        codes[f] = np.array([idx[v] for v in vals], dtype=np.int64)
        cards[f] = len(uniq)
    return y, codes, cards


def levels(cards):
    """Coarsening grid, fixed structurally by the prereg: order by cardinality
    descending, ties by feature name ascending; L_j drops the first j."""
    order = sorted(S, key=lambda f: (-cards[f], f))
    return order, [order[j:] for j in range(len(order) + 1)]


def cell_ids(codes, feats, cards):
    if not feats:
        return np.zeros(len(next(iter(codes.values()))), dtype=np.int64)
    key = np.zeros(len(codes[feats[0]]), dtype=np.int64)
    for f in feats:
        key = key * cards[f] + codes[f]
    _, inv = np.unique(key, return_inverse=True)
    return inv


def plugin(cid, y, n):
    nc = np.bincount(cid).astype(np.float64)
    kc = np.bincount(cid, weights=y).astype(np.float64)
    eps = float(np.sum(kc * (nc - kc) / nc) / n)
    occ = float(np.sum(nc[nc >= 2]) / n)
    ip = float(np.sum(nc * np.abs(2.0 * kc / nc - 1.0)) / n)
    return eps, occ, ip, nc, kc


def cv_tl(cid, y, n, ncell):
    rng = np.random.default_rng(CV_SEED)
    fold = np.empty(n, dtype=np.int64)
    for cls in (0, 1):                      # stratified on the outcome
        idx = np.flatnonzero(y == cls)
        rng.shuffle(idx)
        fold[idx] = np.arange(len(idx)) % K_FOLDS
    nc = np.bincount(cid, minlength=ncell).astype(np.float64)
    kc = np.bincount(cid, weights=y, minlength=ncell).astype(np.float64)
    se = 0.0
    for f in range(K_FOLDS):
        m = fold == f
        nf = np.bincount(cid[m], minlength=ncell).astype(np.float64)
        kf = np.bincount(cid[m], weights=y[m].astype(np.float64), minlength=ncell)
        ntr, ktr = nc - nf, kc - kf
        pi_tr = ktr.sum() / ntr.sum()
        pred_cell = np.where(ntr > 0, np.divide(ktr, ntr, out=np.zeros_like(ktr), where=ntr > 0), pi_tr)
        pred = pred_cell[cid[m]]
        se += float(np.sum((y[m] - pred) ** 2))
    return se / n


def boot_lower_B(nc, kc, n):
    """One-sided 95% lower limit on B via 1000 nonparametric row resamples.
    Resampling rows == multinomial over (cell x label) categories."""
    rng = np.random.default_rng(BOOT_SEED)
    p = np.concatenate([nc - kc, kc]) / n
    K = len(nc)
    out = np.empty(N_BOOT)
    for b in range(N_BOOT):
        d = rng.multinomial(n, p)
        neg, pos = d[:K].astype(np.float64), d[K:].astype(np.float64)
        tot = neg + pos
        ok = tot > 0
        eps = float(np.sum(pos[ok] * neg[ok] / tot[ok]) / n)
        pi = float(pos.sum() / n)
        out[b] = eps / (pi * (1 - pi))
    return float(np.percentile(out, 5.0)), float(np.percentile(out, 50.0))


def U(p_t, sigma, pi):
    d = abs(pi - p_t)
    return (math.sqrt(sigma * sigma + d * d) - d) / (2.0 * (1.0 - p_t))


def main(path):
    y, codes, cards = load(path)
    n = len(y)
    pi = float(y.mean())
    order, grid = levels(cards)
    res = {'n': n, 'pi': pi, 'cardinalities': {f: cards[f] for f in order},
           'order': order, 'levels': []}
    for j, feats in enumerate(grid):
        cid = cell_ids(codes, feats, cards)
        ncell = int(cid.max()) + 1
        eps_pi, occ, ip, nc, kc = plugin(cid, y, n)
        eps_cv = cv_tl(cid, y, n, ncell)
        den = pi * (1 - pi)
        lvl = {'level': f'L{j}', 'features': list(feats), 'K_occupied': ncell,
               'occ': occ, 'I_P': ip,
               'B_pi': eps_pi / den, 'B_cv': eps_cv / den,
               'eps_pi': eps_pi, 'eps_cv': eps_cv}
        lvl['bracket_width'] = lvl['B_cv'] - lvl['B_pi']
        res['levels'].append(lvl)
        print(f"{lvl['level']:>3} K={ncell:>7} occ={occ:.4f} I_P={ip:.4f} "
              f"B_pi={lvl['B_pi']:.4f} B_cv={lvl['B_cv']:.4f} w={lvl['bracket_width']:.4f}",
              flush=True)

    reading = next((l for l in res['levels'] if l['occ'] >= OCC_MIN), None)
    res['reading_level'] = reading['level'] if reading else None
    if reading is None:
        res['verdict'] = 'D'; res['reason'] = 'no level reaches occ >= %.2f' % OCC_MIN
        return res

    j = int(reading['level'][1:])
    cid = cell_ids(codes, grid[j], cards)
    _, _, _, nc, kc = plugin(cid, y, n)
    B_L, B_med = boot_lower_B(nc, kc, n)
    reading['B_L'] = B_L
    reading['B_boot_median'] = B_med

    sig_ours = math.sqrt(pi * (1 - pi) * max(0.0, 1 - B_L))
    sig_naive = math.sqrt(pi * (1 - pi))
    rows = []
    for p_t in P_T_GRID:
        uo, un = U(p_t, sig_ours, pi), U(p_t, sig_naive, pi)
        rows.append({'p_t': p_t, 'U_ours': uo, 'U_naive': un,
                     'ratio': un / uo if uo > 0 else float('inf'),
                     'delta_overlap': (uo <= DELTA_HI) and (un > DELTA_LO)})
    res['bound_table'] = rows
    res['sigma_ours'], res['sigma_naive'] = sig_ours, sig_naive

    R1 = any(r['ratio'] >= 2.0 for r in rows)
    R2 = any(r['ratio'] >= 2.0 and r['delta_overlap'] for r in rows)
    R3 = (B_L >= B_MIN) and (pi <= PI_MAX)
    Da = False
    Db = reading['bracket_width'] > BRACKET_MAX
    Dc = (not Db) and (B_L < B_MIN)
    res.update({'R1': R1, 'R2': R2, 'R3': R3, 'D_a': Da, 'D_b': Db, 'D_c': Dc})
    if Db:
        res['verdict'] = 'D'
    elif R1 and R2 and R3:
        res['verdict'] = 'REGION NON-EMPTY'
    else:
        res['verdict'] = 'A' if Dc else 'REGION EMPTY'
    return res


if __name__ == '__main__':
    out = main(sys.argv[1])
    print(json.dumps(out, indent=1, default=float))

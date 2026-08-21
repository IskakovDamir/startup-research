#!/usr/bin/env python3
"""Demonstration run 2, against 04-experiments/02-PREREG-2.md.

Core estimators are imported from run.py unchanged; only the constants the
pre-registration changed (seeds, threshold grid, clause set) are set here.
"""
import csv, json, math, sys, os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import run as core

# ---- constants fixed by pre-registration 2 (do not edit) --------------------
core.CV_SEED, core.BOOT_SEED = 20260822, 20260823
core.N_BOOT, core.K_FOLDS = 1000, 5
NEAR_MULT = [0.50, 0.75, 1.00, 1.50, 2.00]      # times pi-hat
FAR_GRID = [0.10, 0.20, 0.30, 0.50]
DELTA_LO, DELTA_HI = 0.001, 0.05                 # unchanged from prereg 1
OCC_MIN, BRACKET_MAX, B_MIN = 0.90, 0.25, 0.5    # unchanged from prereg 1
PI_LO, PI_HI = 0.005, 0.03                       # new: base-rate corridor
POSMASS_MIN = 0.50                               # new: D-d
RATIO_MIN = 2.0

# ---- declared feature set S (declared in 02b-DATASET-CHOICE-2.md) -----------
S = ['first_crash_type', 'trafficway_type', 'traffic_control_device',
     'weather_condition', 'lighting_condition', 'roadway_surface_cond',
     'road_defect', 'alignment']
TARGET = 'most_severe_injury'
POSITIVE = {'FATAL', 'INCAPACITATING INJURY'}


def load(path, dedup=False):
    with open(path, newline='') as fh:
        rows = [r for r in csv.DictReader(fh) if (r.get(TARGET) or '').strip()]
    if dedup:
        seen, keep = set(), []
        for r in rows:
            k = tuple((r[f] or '').strip() for f in S) + ((r[TARGET] or '').strip(),)
            if k in seen:
                continue
            seen.add(k); keep.append(r)
        rows = keep
    y = np.array([1 if (r[TARGET] or '').strip().upper() in POSITIVE else 0 for r in rows],
                 dtype=np.int64)
    codes, cards = {}, {}
    for f in S:
        vals = [((r[f] or '').strip() or '__MISSING__') for r in rows]
        uniq = sorted(set(vals)); idx = {v: i for i, v in enumerate(uniq)}
        codes[f] = np.array([idx[v] for v in vals], dtype=np.int64)
        cards[f] = len(uniq)
    return y, codes, cards


def evaluate(y, codes, cards, tag):
    core.S = S
    n = len(y)
    pi = float(y.mean())
    order = sorted(S, key=lambda f: (-cards[f], f))
    grid = [order[j:] for j in range(len(order) + 1)]
    out = {'tag': tag, 'n': n, 'pi': pi, 'order': order,
           'cardinalities': {f: cards[f] for f in order}, 'levels': []}
    for j, feats in enumerate(grid):
        cid = core.cell_ids(codes, feats, cards)
        ncell = int(cid.max()) + 1
        eps_pi, occ, ip, nc, kc = core.plugin(cid, y, n)
        eps_cv = core.cv_tl(cid, y, n, ncell)
        den = pi * (1 - pi)
        posmass = float(np.sum(nc[kc >= 1]) / n)
        lvl = {'level': f'L{j}', 'K_occupied': ncell, 'occ': occ, 'I_P': ip,
               'pos_mass': posmass, 'B_pi': eps_pi / den, 'B_cv': eps_cv / den}
        lvl['bracket_width'] = lvl['B_cv'] - lvl['B_pi']
        out['levels'].append(lvl)
        print(f"[{tag}] {lvl['level']:>3} K={ncell:>6} occ={occ:.4f} posmass={posmass:.4f} "
              f"I_P={ip:.4f} B_pi={lvl['B_pi']:.4f} B_cv={lvl['B_cv']:.4f} "
              f"w={lvl['bracket_width']:.4f}", flush=True)

    reading = next((l for l in out['levels'] if l['occ'] >= OCC_MIN), None)
    out['reading_level'] = reading['level'] if reading else None
    if reading is None:
        out['D_a'] = True; out['verdict'] = 'D'
        return out
    out['D_a'] = False
    j = int(reading['level'][1:])
    cid = core.cell_ids(codes, grid[j], cards)
    _, _, _, nc, kc = core.plugin(cid, y, n)
    B_L, B_med = core.boot_lower_B(nc, kc, n)
    reading['B_L'], reading['B_boot_median'] = B_L, B_med

    sig_ours = math.sqrt(pi * (1 - pi) * max(0.0, 1 - B_L))
    sig_naive = math.sqrt(pi * (1 - pi))
    out['sigma_ours'], out['sigma_naive'] = sig_ours, sig_naive

    def row(p_t, band):
        uo, un = core.U(p_t, sig_ours, pi), core.U(p_t, sig_naive, pi)
        return {'p_t': p_t, 'band': band, 'U_ours': uo, 'U_naive': un,
                'ratio': un / uo if uo > 0 else float('inf'),
                'overlap': (uo <= DELTA_HI) and (un > DELTA_LO)}

    near = [row(m * pi, 'near') for m in NEAR_MULT]
    far = [row(p, 'far') for p in FAR_GRID]
    at_pi = row(pi, 'at_pi')
    out['near'], out['far'], out['at_pi'] = near, far, at_pi

    out['R1p'] = any(r['ratio'] >= RATIO_MIN for r in near)
    out['R2p'] = any(r['ratio'] >= RATIO_MIN and r['overlap'] for r in near)
    out['R3p'] = (B_L >= B_MIN) and (PI_LO <= pi <= PI_HI)
    out['R1pp'] = at_pi['ratio'] >= RATIO_MIN
    out['D_b'] = reading['bracket_width'] > BRACKET_MAX
    out['D_c'] = (not out['D_b']) and (B_L < B_MIN)
    out['D_d'] = reading['pos_mass'] < POSMASS_MIN
    far_flip = any(r['ratio'] >= RATIO_MIN and r['overlap'] for r in far)
    out['D_e'] = (not out['R1p']) and far_flip
    out['far_flip'] = far_flip

    if out['D_b'] or out['D_d']:
        out['verdict'] = 'D'
    elif out['D_e']:
        out['verdict'] = 'D (repeat of run 1: flip only far from the base rate)'
    elif out['R1p'] and out['R2p'] and out['R3p']:
        out['verdict'] = 'REGION NON-EMPTY NEAR THE BASE RATE'
    else:
        out['verdict'] = 'A' if out['D_c'] else 'REGION EMPTY'
    out['margins'] = {'occ': reading['occ'] / OCC_MIN - 1,
                      'bracket': 1 - reading['bracket_width'] / BRACKET_MAX,
                      'B_L': B_L / B_MIN - 1}
    return out


if __name__ == '__main__':
    path = sys.argv[1]
    main_res = evaluate(*load(path, dedup=False), tag='as-given')
    dedup_res = evaluate(*load(path, dedup=True), tag='dedup')
    fragile = (main_res.get('R1p') != dedup_res.get('R1p')
               or main_res.get('R3p') != dedup_res.get('R3p')
               or main_res.get('D_b') != dedup_res.get('D_b'))
    final = main_res['verdict'] if not fragile else 'D (fragile under declared deduplication)'
    print(json.dumps({'as_given': main_res, 'dedup': dedup_res,
                      'dedup_flips_a_clause': fragile, 'final_verdict': final},
                     indent=1, default=float))

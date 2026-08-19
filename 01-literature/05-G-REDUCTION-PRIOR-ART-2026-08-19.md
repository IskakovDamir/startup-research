# СВЕДЕНИЕ NET BENEFIT И COST-LOSS К ОДНОЙ ВЕЛИЧИНЕ — проверка на занятость

> Составлено 2026-08-19. Проверялся единственный кандидат на самостоятельный результат из `00-context/05-SIZE-ASSESSMENT.md`.
> Проверка проведена **до написания заметки**, как и было условлено. Это тот случай, ради которого условие ставилось.

---

# ВЕРДИКТ

**ОПУБЛИКОВАНО.** `[REF: Baker, Cook, Vickers & Kramer 2009]`, «Using Relative Utility Curves to Evaluate Risk Prediction», Journal of the Royal Statistical Society Series A, 172(4):729–748. Полный текст прочитан `[FETCH: https://pmc.ncbi.nlm.nih.gov/articles/PMC2804257/ · 2026-08-19]`.

**Соавтор — Vickers**, то есть автор самого decision curve analysis. Сведение сделано внутри той же линии, а не в соседней.

---

## Что именно там есть

Обе величины выведены из **одного** выражения для ожидаемой полезности, зависящего от четырёх базовых полезностей **только через порог риска**, и различаются нормировкой.

**Net benefit — нормировка на истинно-положительные:**

> «Vickers et al (2006) proposed the net benefit as a function of the expected utility that depends on the four basic utilities only through the risk threshold without the need for additional assumptions.» `[FETCH: · 2026-08-19]`

> «Setting P = 1 as reference level means that net benefit is measured in units of true positives. Setting j = j(R) means evaluation is at risk threshold R.» `[FETCH: · 2026-08-19]`

**Relative utility — нормировка на оракула:**

> «a new function of expected utilities, called the relative utility, that is a function of the four basic utilities only through the risk threshold but, **unlike net benefit, does not require a reference value for any utility**. In particular, the relative utility is the **maximum fraction of expected utility achieved by risk prediction as compared with perfect prediction**.» `[FETCH: · 2026-08-19]`

и то же во второй работе линии, `[REF: Baker 2009]`, JNCI:

> «relative utility is the fraction of the expec[ted utility] ... obtained by the risk prediction model at the optimal cut point» `[FETCH: https://pmc.ncbi.nlm.nih.gov/articles/PMC2778669/ · 2026-08-19]`

**«Нормировка на совершенный прогноз при пороге» — это ровно `VS = (E_b − E_f)/(E_b − E_p)` из cost-loss.** Различие с метеорологической линией — в названии («relative utility» против «relative value») и в дисциплине, не в объекте.

## Более общий дом — тот же, что назвал PI

`[REF: Reid & Williamson 2009]`, «Information, Divergence and Risk for Binary Experiments», arXiv 0901.0356, **абстракт дословно через arXiv API** `[FETCH: http://export.arxiv.org/api/query?id_list=0901.0356 · 2026-08-19, только абстракт]`:

> «We unify f-divergences, Bregman divergences, surrogate loss bounds (regret bounds), proper scoring rules, matching losses, cost curves, ROC-curves and information. We do this by systematically studying integral and variational representations of these objects and in so doing **identify their primitives which all are related to cost-sensitive binary classification**.»

То есть пороговая cost-sensitive потеря — признанный примитив, через интегральные представления которого выражается всё семейство, включая proper scoring rules и cost curves. Это линия Schervish, которую PI и назвал наиболее вероятным местом. **Названо верно.**

Полный текст не открывался: PDF отваливался по таймауту дважды, ar5iv и HTML-рендер не взялись. Поэтому эта работа здесь **на уровне абстракта** и несёт только указание на дом, а не доказательство.

---

## Что это убивает и что оставляет

**Убито:** сведение net benefit и cost-loss relative value к одной величине как самостоятельный результат. Заявлять его нельзя ни в какой форме. Опубликовано в 2009 году соавтором DCA, и сверх того является частным случаем признанного примитива.

**Осталось ровно три вещи, и первая из них не проверена:**

1. **Граница `G ≤ σ/2` при `σ² = π(1−π)(1−B)`** — связь достижимого выигрыша с **долей объекта**. У Baker et al. никакой оценки неустранимой доли нет: у них нормировка на оракула, то есть предел предполагается достигнутым, а не оценивается. **НО:** это оценка зазора Йенсена вогнутой функции через дисперсию, а соответствия «статистическая информация ↔ f-дивергенции» — ровно та литература, где такие границы живут. **Не проверено. Проверять до любого следующего шага.**
2. **Область `(B, π, δ)`** — следствие пункта 1. Живёт или умирает вместе с ним.
3. **Требование направления и инверсия оценщика** — абзац, посылки которого 1961, 1966, 1973 и 2020.

## Следствие для размера — надо признать прямо

Прогноз PI подтвердился дословно: остаётся **область плюс абзац**, и это **комментарий, а не заметка**. Причём область висит на непроверенной границе, а абзац — на четырёх чужих посылках.

Правка размера внесена в `00-context/05-SIZE-ASSESSMENT.md` в этой же сессии.

## Что осталось непроверенным

- **Граница `G ≤ σ/2` — не проверялась.** Первоочередное; проверять в линии DeGroot / Schervish / Reid & Williamson и в литературе связи статистической информации с дивергенциями.
- Reid & Williamson прочитан только по абстракту.
- Прямого сопоставления «relative utility (медицина) = relative value (метеорология)» в тексте Baker et al. я не искал специально; для вердикта это не нужно, объект и так совпал.

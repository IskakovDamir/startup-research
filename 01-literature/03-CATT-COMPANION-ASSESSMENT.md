# КОМПАНЬОН CATT — оценка

> **Статус:** закрыто 2026-08-18. Последний документ, стоявший между уцелевшим утверждением и чистым вердиктом.
> **Что читалось.** Полные тексты двух версий, не абстракты.

---

# ВЕРДИКТ

**Остаточный зазор ОТКРЫТ.**

**И отдельно, повышено 2026-08-19: величина Catt направлена не в ту сторону, чтобы быть конкурентом.** Раздел ниже стоял предпоследним в этом файле. Это было неверное место — из всего, что дал разбор компаньона, это самое существенное.

---

# НАПРАВЛЕННОСТЬ ОЦЕНКИ — главное в этом файле

> Повышено из предпоследнего раздела 2026-08-19. Все цитаты переустановлены фетчем в этой сессии: `[FETCH: https://arxiv.org/pdf/2601.10006v5 · 2026-08-19]`. Фетч прошлой сессии не засчитывается.

AMI — оценка **снизу** на доступную зависимость, а не оценка потолка. Автор говорит это прямым текстом, в разделе ограничений:

> «The reading is therefore one-sided: high AMI evidences recoverable structure, whereas low AMI does not establish its absence.» `[FETCH: https://arxiv.org/pdf/2601.10006v5 · 2026-08-19]`

и раньше, там, где объясняет смысл меры:

> «Low AMI does not mean a series should not be forecast; it means the measured single-lag dependence is weak at the relevant horizon, so any forecasting skill must come from information beyond that signal» `[FETCH: https://arxiv.org/pdf/2601.10006v5 · 2026-08-19]`

## Почему это структурно, а не оговорка: четыре механизма, все в тексте v5

1. **Информационное множество диагностики — строгое подмножество того, на что смотрят модели.** Дословно: «Because every probe conditions on more than the diagnostic does, and N-BEATS additionally pools across series, the reported associations are conservative: a single-lag within-series statistic ranks the realised error of models with strictly greater access.» `[FETCH: https://arxiv.org/pdf/2601.10006v5 · 2026-08-19]` Диагностика видит один лаг, а не объявленное информационное множество целиком. Автор сам перечисляет, откуда низко-AMI ряд всё ещё может быть предсказуем: «from the remainder of the series history, from structure visible only in combinations of lags, from pooled estimation across related series, or from external drivers, hierarchy, or calendar effects the screen cannot capture» `[FETCH: https://arxiv.org/pdf/2601.10006v5 · 2026-08-19]`.
2. **Оценка усечена нулём снизу, и ровно в низком конце.** «raw estimates on white noise are centred on zero at every length (mean −0.0002 nats at T = 48 and +0.0010 at T = 240, with 50 to 57% of raw estimates negative), so the near-zero truncated floor reflects an unbiased estimator rather than a property manufactured by the truncation rule» `[FETCH: https://arxiv.org/pdf/2601.10006v5 · 2026-08-19]`. Оговорка написана в защиту от обвинения в артефакте усечения, и в этом качестве она убедительна. Но следствие для нас другое: около нуля — то есть ровно там, где сидел бы останавливающий вердикт, — сырая оценка отрицательна примерно в половине случаев, и разрешающей способности у величины там нет.
3. **Инференциальный аппарат односторонен по построению.** Нуль — перестановочный: «a permutation test can only exclude an exactly zero association, so statistical significance here carries no evidence of practical magnitude» `[FETCH: https://arxiv.org/pdf/2601.10006v5 · 2026-08-19]`. Такой тест отвергает нулевую зависимость и никогда её не устанавливает.
4. **Порог выборочно-относительный** — терцили в v4, децили в v5, см. (b) ниже. Даже при верном направлении «низкий» определён относительно распределения этой же выборки.

Механизмы независимы: устранение любого одного асимметрию не снимает.

## Что из этого следует — и чего НЕ следует

**Следует.** Линия Catt не выдаёт вердикта «остаток в объекте, не разворачивайте» даже во временных рядах. Значит она не конкурент за величину блока 2, и это основание прочнее, чем «у него временные ряды»: постановку снимет его же следующая работа, направление оценщика — нет. Перенос AMI в поперечник унаследовал бы асимметрию вместе с оценщиком.

**Не следует, что у Catt ошибка.** Популяционная величина F(h; I_t) в теоретической работе — настоящий потолок относительно объявленного I_t, и останавливающая логика при ней корректна: «when forecastability is near zero, all methods converge toward the same floor» `[FETCH: https://arxiv.org/html/2603.27074v1 · 2026-08-19]`. Разрыв между теоремой и оценщиком автор не прячет — он его перечисляет сам. Писать это как обнаруженный нами дефект — передёргивание, которое снимут. Писать надо как **разграничение того, какие вердикты какая величина способна нести**.

**И следует то, что бьёт по нам.** Тот же фильтр применяется к блоку 2: наша оценка обязана ограничивать долю объекта снизу и обязана объявить направление. Точка, названная потолком, вердикта не несёт. См. `00-context/00-THESIS.md`, раздел «Направленность оценки», и открытую точку отказа там же.

---

## Что именно найдено и почему это не тот документ, который ожидался

Ссылка [3] в теоретической работе `[REF: Catt 2026]` ведёт на SSRN. SSRN закрыт Cloudflare, `curl` получает страницу-заглушку «Just a moment...», DOI отдаёт 403 `[проверено 2026-08-18]`.

Обход нашёлся не в SSRN. **У Peter Maurice Catt на arXiv три работы, а не одна:**

- `2601.10006` — «Horizon-resolved Forecastability of Time Series via Auto Mutual Information»
- `2603.20546` — «On the Limits of Prediction: Forecastability Profiles and Information Decay in Time Series». Поле comment: «Resubmitted as a highly revised paper — Forecastability as an Information-Theoretic Limit on Prediction [arXiv:2603.27074]». То есть это предшественник уже прочитанной теоретической работы, а не компаньон.
- `2603.27074` — теоретическая работа, разобранная в `02-CATT-2026-ASSESSMENT.md`.

**Компаньон — это `2601.10006`.** Отождествление с SSRN-записью установлено по совпадению содержания, а не по заявлению автора: аннотация SSRN, полученная через Crossref `[FETCH: https://api.crossref.org/works/10.2139/ssrn.6416626 · 2026-08-18]`, описывает валидацию «across 42,355 time series spanning six temporal frequencies» против «realized out-of-sample symmetric mean absolute percentage error» — ровно то, что теоретическая работа приписывает компаньону, и ровно то, что содержат версии v1–v4 arXiv-препринта. Заголовки при этом разные, и **тождество остаётся выводом, а не подтверждённым фактом**; SSRN лично не открыт.

Читались обе релевантные версии:
- `v4` — соответствует SSRN по объёму данных и метрике `[FETCH: https://arxiv.org/pdf/2601.10006v4 · 2026-08-18]`
- `v5` — текущая `[FETCH: https://arxiv.org/pdf/2601.10006v5 · 2026-08-18]`

### Побочная находка, которая важнее, чем выглядит

Поле comment у v5: «Substantially revised and rescoped to M4 Monthly under an official-holdout protocol. **Supersedes the six-frequency analysis of v1 to v4**».

Теоретическая работа `2603.27074` (март 2026) цитирует компаньона так: «Spearman rank correlations of −0.41 to −0.72 with out-of-sample sMAPE for five of six temporal frequencies». Это числа снятой шестичастотной версии.

Текущая v5 (август 2026), пересчитанная под официальный holdout-протокол на M4 Monthly, сообщает «mean Spearman ρ of 0.11 to 0.13 for ETS and N-BEATS» и характеризует связь как «modest but systematic».

**То есть эмпирическая опора линии forecastability между версиями заметно просела, а теоретическая работа продолжает цитировать снятые числа.** Это не наш аргумент против Catt в тексте — но при цитировании его эмпирики опираться следует на v5, а не на числа из теоретической работы.

---

## (a) Есть ли шаг решения

**Да, в версии v4 — и он развит сильнее, чем что-либо у Catt в теоретической работе.**

v4 заявляет это как основной вклад:

> «It operationalises this construct using auto-mutual information estimated via a non-parametric k-nearest-neighbour framework, providing a practical method for classifying series into action categories (invest in modelling / model cautiously / manage uncertainty) based on ex-ante forecastability assessment. **This diagnostic classification framework is the primary contribution for decision support.**»

и ставит вопрос прямо в нашей форме:

> «The diagnostic addresses not 'which model is best?' but **'is this series worth modelling at all at the decision horizon?'**»

Есть раздел «Implications for Decision Workflows» с конкретными предписаниями:

> «Series with low AMI or unstable AMI estimation are better served by simple baselines. For these series, resources should shift from forecast refinement toward consequence mitigation: safety stock sizing, scenario planning, cadence adjustment, or decision architectures that are robust to forecast error.»

и явное **gating rule**:

> «This leads to a practical gating rule: multivariate enrichment should be attempted only when univariate forecastability is low but plausible external drivers exist at the decision horizon.»

**В версии v5 этот шаг снят.** Дословно:

> «One implication lies outside the present claims: a pre-modelling forecastability measure of this kind could inform where additional modelling effort is likely to encounter exploitable temporal structure, and **developing and evaluating such decision layers is future work.**»

То есть автор в текущей редакции сам вынес слой решения за пределы работы.

## (b) Взвешивает ли он цены ошибок и базовую ставку — и какую из двух

**Ни ту, ни другую. Это ответ, от которого зависит весь остаток, и он проверен двумя способами.**

Поиск по полному тексту v4 по терминам false positive, false negative, asymmetry цены, base rate, prevalence, utility, loss function, expected cost, net benefit, misclassification даёт **ноль содержательных вхождений**. Единственные совпадения на «asymmetry» относятся к временнóму разделению обучения и оценки в протоколе, а не к ценам ошибок.

Категории действия задаются **терцилями собственного эмпирического распределения диагностики**: «series are partitioned into Low, Medium, and High AMI terciles and median sMAPE is compared across terciles». Порог не выводится ни из цен ошибок, ни из частоты исхода — он выводится из того, как распределилась сама метрика в этой выборке. В v5 это названо прямо как ограничение: «the decile assignments are sample-relative and not portable to a new portfolio without recalibration against its own series distribution; a data-independent forecastability scale remains an open problem».

Базовой ставки в этой постановке **нет как объекта**: исход непрерывный, метрика sMAPE и MASE, бинарного события не существует, поэтому нечему иметь базовую ставку.

И автор сам выносит теоретико-решающую потерю за пределы работы:

> «This study also focuses exclusively on point forecast accuracy measured via sMAPE; probabilistic forecasting, density forecast evaluation, **and decision-theoretic loss functions may exhibit different relationships with AMI.**»

## (c) Затрагивает ли фирмы, организации или любую поперечную постановку

**Нет.** Рамка применения названа организационной («organizational forecasting contexts» в аннотации SSRN), и последствия описаны операционные — страховой запас, сценарное планирование. Но **единица наблюдения везде временной ряд**, не фирма. Поперечной постановки нет ни в одной версии. Ближайшее к расширению — рассуждение о многомерности, и оно остаётся внутри временных рядов: «univariate forecastability is a necessary, though not sufficient, condition for value creation in multivariate models».

## (d) Выходит ли валидация за пределы одномерных временных рядов

**Нет.** v4 — соревновательный корпус M4, шесть частот, зонды Seasonal Naïve, ETS, N-BEATS. v5 — M4 Monthly, официальный holdout. Всё одномерные временные ряды. Ограничение автора:

> «Validation used three specific forecasting methods on M4 data. While the conceptual framework is general, empirical relationships are context-dependent, and domain-specific validation remains essential before operational deployment.»

---

## Отдельно: величина Catt не может выдать останавливающий вердикт даже у себя дома

**Раздел повышен наверх 2026-08-19 и развёрнут** — см. «НАПРАВЛЕННОСТЬ ОЦЕНКИ» сразу после вердикта. Здесь он стоял предпоследним, и это было неверное место.

---

# ЧТО ОСТАЁТСЯ НЕЗАНЯТЫМ — одно предложение

> Ни один опубликованный критерий не задаёт **порог решения из отношения цены ложноположительного к цене ложноотрицательного и из базовой ставки исхода**, имея при этом внутри **полученную из данных оценку неустранимой доли ошибки при обусловливании на объявленном наборе признаков**: критерии, задающие порог именно так — decision curve analysis и cost-loss relative value, — не содержат никакой оценки неустранимой компоненты, а работы, которые её оценивают — ILD, триаж Catt по AMI, completeness, — задают порог из собственного выборочного распределения диагностики либо не задают его вовсе.

Проверка против враждебного рецензента, прочитавшего всё пятерное:

- **Vickers & Elkin** — порог из отношения вреда, базовая ставка в net benefit, вердикт против стратегий без модели. Оценки неустранимой компоненты нет вообще.
- **Perdomo ICML 2024** — решение есть, но доля объяснённой дисперсии входит **параметром**, не оценивается.
- **ILD (arXiv 2107.11609)** — оценивает пол для бинарного исхода при категориальных признаках, решения «прекратить поиск модели» и «обогатить данные» заявлены. Ни цен ошибок, ни базовой ставки, ни сравнения с решением без модели.
- **Catt, компаньон** — оценка есть, решение есть в v4 и снято в v5, порог терцильный, цен ошибок нет, базовой ставки нет как объекта.
- **Линия SMJ** — оценивает компоненты дисперсии исхода внутри выборки, остаток не печатает, решения не выдаёт.
- **ease.ml/snoopy `[REF: Renggli et al. 2020]` — добавлено в проверку 2026-08-19.** Оценивает байесовскую ошибку из данных относительно объявленного представления признаков **и** привязывает её к решению — feasibility study перед разработкой. Ближайший из всех проверенных. Не ломает предложение по двум причинам: решение сравнивается с заданной пользователем целевой точностью `α_target`, а не с порогом из цен ошибок, и базовой ставки в нём нет; плюс полярность обратная — их оценка обязана **не занижать** неустранимую ошибку, наша обязана занижать.
- **Корпус resubstitution `[REF: Cochran & Hopkins 1961]`, `[REF: Hills 1966]`, `[REF: Glick 1973]`, `[REF: Braga-Neto & Dougherty 2009]` — добавлен в проверку 2026-08-19.** Даёт и оценку снизу на байесовскую ошибку, и её скорость, и зажим — но никакого решения. Смещение там всюду дефект, подлежащий устранению.

Пересечение пусто. Предложение выдерживает — но набор проверенных вырос с пяти позиций до семи, и обе новые ближе прежних. Дальнейшее сужение обязано идти не по «оценки нет», а по **порогу и полярности**: это единственные два квалификатора, которые ещё держат.

---

## Честная оценка того, что это значит

Зазор открыт, но он стал **зазором в задании порога**. Уцелевший вклад формулируется так: взять оценённую долю объекта и поместить её внутрь алгебры порога чистой выгоды, показав область параметров, в которой вердикт переворачивается.

Это определённо, проверяемо и скромно. Это не «мы вводим мысль о неустранимой ошибке» — этой рамки больше нет. Достаточно ли этого для работы — решение PI, но объём вклада теперь виден целиком и не должен переоцениваться при планировании.

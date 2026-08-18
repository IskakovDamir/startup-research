# КОМПАНЬОН CATT — оценка

> **Статус:** закрыто 2026-08-18. Последний документ, стоявший между уцелевшим утверждением и чистым вердиктом.
> **Что читалось.** Полные тексты двух версий, не абстракты.

---

# ВЕРДИКТ

**Остаточный зазор ОТКРЫТ.**

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

Это надо занести, потому что меняет оценку угрозы. v5, дословно:

> «Low AMI does not mean a series should not be forecast; it means the measured single-lag dependence is weak at the relevant horizon, so any forecasting skill must come from information beyond that signal»

> «The reading is therefore **one-sided: high AMI evidences recoverable structure, whereas low AMI does not establish its absence.**»

AMI — оценка **снизу** на доступную зависимость, а не оценка потолка. Из неё следует «здесь структура есть», но не следует «здесь структуры нет». То есть в текущей редакции линия Catt не поддерживает вывод «остаток в объекте, остановитесь» **даже для временных рядов**, а диагностика видит лишь одно лаговое наблюдение, а не объявленное информационное множество целиком.

---

# ЧТО ОСТАЁТСЯ НЕЗАНЯТЫМ — одно предложение

> Ни один опубликованный критерий не задаёт **порог решения из отношения цены ложноположительного к цене ложноотрицательного и из базовой ставки исхода**, имея при этом внутри **полученную из данных оценку неустранимой доли ошибки при обусловливании на объявленном наборе признаков**: критерии, задающие порог именно так — decision curve analysis и cost-loss relative value, — не содержат никакой оценки неустранимой компоненты, а работы, которые её оценивают — ILD, триаж Catt по AMI, completeness, — задают порог из собственного выборочного распределения диагностики либо не задают его вовсе.

Проверка против враждебного рецензента, прочитавшего всё пятерное:

- **Vickers & Elkin** — порог из отношения вреда, базовая ставка в net benefit, вердикт против стратегий без модели. Оценки неустранимой компоненты нет вообще.
- **Perdomo ICML 2024** — решение есть, но доля объяснённой дисперсии входит **параметром**, не оценивается.
- **ILD (arXiv 2107.11609)** — оценивает пол для бинарного исхода при категориальных признаках, решения «прекратить поиск модели» и «обогатить данные» заявлены. Ни цен ошибок, ни базовой ставки, ни сравнения с решением без модели.
- **Catt, компаньон** — оценка есть, решение есть в v4 и снято в v5, порог терцильный, цен ошибок нет, базовой ставки нет как объекта.
- **Линия SMJ** — оценивает компоненты дисперсии исхода внутри выборки, остаток не печатает, решения не выдаёт.

Пересечение пусто. Предложение выдерживает.

---

## Честная оценка того, что это значит

Зазор открыт, но он стал **зазором в задании порога**. Уцелевший вклад формулируется так: взять оценённую долю объекта и поместить её внутрь алгебры порога чистой выгоды, показав область параметров, в которой вердикт переворачивается.

Это определённо, проверяемо и скромно. Это не «мы вводим мысль о неустранимой ошибке» — этой рамки больше нет. Достаточно ли этого для работы — решение PI, но объём вклада теперь виден целиком и не должен переоцениваться при планировании.

# VERIFIED SOURCES — с уровнем провенанса

> **Правило файла.** Каждая запись помечена уровнем провенанса. Ничего не переносится отсюда в прозу без проверки уровня.
> **Уровни:**
> - `[FETCHED]` — страница открыта в сессии, содержание прочитано.
> - `[SEARCH-SNIPPET]` — подтверждено сниппетом поиска: заголовок, авторы, год, площадка, URL. Содержание за пределами сниппета НЕ подтверждено.
> - `[CITATION-ONLY]` — встречено только в списке литературы другой работы. Существование правдоподобно, детали НЕ подтверждены. **Нельзя цитировать.**
>
> Сессия верификации: 2026-08-18.

---

## Якорные работы тезиса

### Salganik et al. 2020 — предсказуемость жизненных траекторий
`[SEARCH-SNIPPET]` · PNAS 117(15):8398–8403 · https://www.pnas.org/doi/10.1073/pnas.1915006117 · DOI 10.1073/pnas.1915006117

Подтверждено: 160 команд, common task method, шесть жизненных исходов, данные Fragile Families and Child Wellbeing Study. Лучшие предсказания оказались неточными и лишь слегка лучше простого бенчмарка. **Ключевое для нас:** ошибка предсказания сильно связана с тем, какую семью предсказывают, и слабо — с применённой техникой.

**Роль в проекте.** Прецедент декомпозиции «объект против метода». Блок 2 — перенос этой логики на фирмы. Отличие, которое надо признавать: у них разнообразие методов из 160 независимых команд, у нас из собственного зоопарка.

**Есть correction:** PNAS 118(50):e2118703118 (2021). Проверить перед цитированием.

---

### Otis, Clarke, Delecourt, Holtz, Koning 2026 — GenAI и результативность предпринимателей
`[SEARCH-SNIPPET]` · Management Science · DOI 10.1287/mnsc.2024.06909 · также HBS WP и SSRN 4671369

Подтверждено: полевой эксперимент, кенийские предприниматели, GPT-4-ментор в WhatsApp против стандартного бизнес-гайда. Средний эффект на выручку и прибыль не отвергает ноль. Эффект для слабых на старте более чем на 0,20 SD ниже, чем для сильных. Слабые ≈ на 10% хуже, сильные ≈ +15%. Разница не от того, какие вопросы задавали и какие советы получали, а от того, какие советы **отбирали и внедряли**.

**Роль в проекте.** Причинное доказательство, что ИИ-ассистирование может вредить. Гетерогенность **по пользователю** уже установлена. Наш незакрытый кусок: гетерогенность **по структуре задачи**, считаемая заранее.

**Расхождение в цифрах между версиями:** SSRN-препринт даёт «около 0,25 SD», журнальная версия «более 0,20 SD». Цитировать журнальную.

---

## Performative prediction

`[CITATION-ONLY]` — встречены только в reference lists сторонних arXiv-работ:
- Perdomo, "The Relative Value of Prediction in Algorithmic Decision Making", ICML 2024
- Miller, Perdomo, Zrnic, "Outside the echo chamber: Optimizing the performative risk", ICML 2021
- Mendler-Dünner, Perdomo, Zrnic, Hardt, "Stochastic optimization for performative prediction", NeurIPS 2020

**СТАТУС: требуют собственного fetch до любого использования.** Это ядро блока 3 — верифицировать первым делом.

---

## Контекст поля (для позиционирования, не для тезиса)

### Kleinberg, Ludwig, Mullainathan, Obermeyer 2015
`[SEARCH-SNIPPET]` · American Economic Review 105(5):491–495 · https://www.aeaweb.org/articles?id=10.1257/aer.p20151023
Класс задач, где нужна предсказательная, а не причинная инференция. Рамка «prediction policy problem» — наш критерий развёртывания живёт именно в этой рамке.

### Mullainathan & Spiess 2017
`[SEARCH-SNIPPET]` · Journal of Economic Perspectives 31(2):87–106
Различение prediction против estimation.

### Athey & Imbens 2019
`[SEARCH-SNIPPET]` · Annual Review of Economics 11:685–725 · препринт https://arxiv.org/pdf/1903.10075

### Chernozhukov et al. 2018 — Double/Debiased ML
`[SEARCH-SNIPPET]` · The Econometrics Journal 21(1):C1–C68

### Gentzkow, Kelly, Taddy 2019 — Text as Data
`[SEARCH-SNIPPET]` · Journal of Economic Literature 57(3):535–574 · https://www.aeaweb.org/articles?id=10.1257/jel.20181020

---

## Предсказание успеха стартапов — состояние поля

### Maarouf, Feuerriegel, Pröllochs 2025
`[SEARCH-SNIPPET]` · European Journal of Operational Research 322(1):198–214 · препринт https://arxiv.org/abs/2409.03668
Fused LLM, N=20 172 профиля Crunchbase. Текст самоописания даёт часть предсказательной силы.

### Leakage-Controlled, Calibration-First Evaluation 2026
`[SEARCH-SNIPPET]` · Information (MDPI) 17(7):702 · DOI 10.3390/info17070702
Удаление признаков, накапливающих исход, снижает AUROC на 0,05–0,09 на выборке 66 368 фирм и на 0,19 на инженерной выборке 923 фирм. Независимая работа на тех же 923 без leakage-контроля отчитывалась о 88,1% accuracy.
**Роль:** обоснование, почему блок 1 обязан быть as-of. Не наш вклад, наша гигиена.

### Nanda, Samila, Sorenson — персистентность VC
`[SEARCH-SNIPPET]` · Journal of Financial Economics
Ранний успех фонда во многом объясняется тем, что он оказался в нужной индустрии и регионе в нужное время; дальше работает доступ к сделкам.
**Роль:** источник тривиального примитива для аргумента 1 (экспозиция сектор × стадия × год × капитал).

### Korteweg & Sorensen — skill and luck in PE
`[CITATION-ONLY]` — встречено только как цитата в чужих списках. Не цитировать до fetch.

---

## Не подтверждено, не использовать

- Hassan et al., "Text as Data in Economic Analysis", JEP 2025 — `[CITATION-ONLY]`
- Kapoor & Narayanan, Patterns 2023 (leakage) — `[CITATION-ONLY]` в этой сессии
- SSFF, R.A.I.S.E., Beyond Isolated Investor, CrunchLLM — `[SEARCH-SNIPPET]` на уровне существования; содержание не проверено. Нужны только для абзаца «поле перегрето», не для утверждений.

---

# СЕССИЯ ВЕРИФИКАЦИИ 2026-08-18 (вторая) — корпус критериев развёртывания

> Всё в этом разделе получено фетчем в сессии 2026-08-18. Уровень указан у каждой записи. Записи `[FETCHED]` открывались и читались; для двух из них текст извлекался локально из PDF, что помечено отдельно.

## Perdomo — Revisiting the Predictability of Performative, Social Events
`[FETCHED · локально из PDF]` · ICML 2025 · https://arxiv.org/pdf/2503.11713

Теорема 5.1: существует distribution map, при котором предиктор проходит все ограниченные тесты валидности и при этом его квадратичная ошибка не меньше ошибки любой функции h под индуцированным ею распределением. Подпись к рис. 1: «While calibrated, these maximize squared error since they induce y to be a fair coin toss.» Абстракт: «we establish that one can always efficiently predict social events accurately, regardless of how predictions influence data».

**Роль в проекте.** Снимает аргумент 4 и центральное утверждение прежней редакции тезиса. См. `00-context/03-SUPERSEDED-THESIS-2026-08-18.md`.

## Perdomo — The Relative Value of Prediction in Algorithmic Decision Making
`[FETCHED · локально из PDF]` · ICML 2024 (строка комментария на arXiv: «accepted to ICML 2024, non-archival track at FORC 2024») · https://arxiv.org/pdf/2312.08511

Prediction-access ratio: отношение предельного выигрыша от улучшения предиктора к выигрышу от расширения доступа. Теорема 1.1 (informal): при линейной модели PAR равен γs/α, где γs² — доля объяснённой дисперсии, α — доля популяции, которую можно охватить. Доля объяснённой дисперсии — **входной параметр**, подставляемый ссылкой на `[REF: Salganik 2020]`. Даёт останавливающий вердикт вида «leave the predictor "as is"».

**Роль в проекте.** Ближайший конкурент по позиционированию и обязательная оговорка к действующему утверждению. Единственный найденный критерий, умеющий останавливать улучшение модели, — но по основанию сравнения рычагов, а не по локализации остатка.

## Vickers & Elkin — Decision curve analysis: a novel method for evaluating prediction models
`[FETCHED]` · Medical Decision Making 2006 · https://pmc.ncbi.nlm.nih.gov/articles/PMC2577036/

Net benefit против стратегий treat-all / treat-none. Порог решения кодирует относительный вред FP против FN.

**Роль в проекте.** Ближайший предшественник аргумента 1 (skill сверх примитива, не требующего модели) и одна из двух опор действующего утверждения (критерий без потолка вообще).

## Sadatsafavi, Lee & Gustafson — Uncertainty and the Value of Information in Risk Prediction Modeling
`[FETCHED]` · Medical Decision Making 2022 · https://pmc.ncbi.nlm.nih.gov/articles/PMC9194963/

Discussion, дословно: «The EVPI as defined in this work represents the uncertainty due to the finite development sample, resulting in uncertainty in the regression coefficients of the prediction model. Importantly, this EVPI does not represent the value of knowing the true risk for each individual, which is also a function of predictors that are unknown, unmeasured, or intentionally left out of the model.»

**Роль в проекте.** Дисклеймер авторов ровно про нашу величину. Опора действующего утверждения со стороны метода.

## Murphy — The Value of Climatological, Categorical and Probabilistic Forecasts in the Cost-Loss Ratio Situation
`[SEARCH-SNIPPET]` · Monthly Weather Review 1977 · https://journals.ametsoc.org/view/journals/mwre/105/7/1520-0493_1977_105_0803_tvocca_2_0_co_2.xml
Полный текст закрыт: сервер вернул 403. Подтверждены заголовок, год, площадка. Содержание за пределами сниппета НЕ подтверждено — **не цитировать дословно**.

## CAWCR / WWRP-WGNE Forecast Verification — Issues, Methods and FAQ
`[FETCHED]` · https://www.cawcr.gov.au/projects/verification/verif_web_page.html

Relative value: «For a cost/loss ratio C/L for taking action based on a forecast, what is the relative improvement in economic value between climatological and perfect information?» Skill score: «the reference forecast is usually persistence (no change from most recent observation) or climatology».

**Роль в проекте.** Опора действующего утверждения со стороны оракульного нормировщика; используется вместо закрытого текста Murphy 1977 там, где нужна дословная формулировка.

## Правка к прежним записям

- Perdomo, «The Relative Value of Prediction in Algorithmic Decision Making» — прежний уровень `[CITATION-ONLY]` снят, теперь `[FETCHED]`, год ICML 2024 подтверждён.
- Miller/Perdomo/Zrnic ICML 2021 и Mendler-Dünner et al. NeurIPS 2020 остаются `[CITATION-ONLY]`: подтверждены только строкой в списке публикаций автора, собственный fetch работ не делался.

---

# СЕССИЯ 2026-08-18 (третья) — гейт идентифицируемости

## Yan & Rahal — On the Unknowable Limits to Prediction
`[FETCHED · препринт прочитан целиком локально из PDF]` · Nature Computational Science 2025; препринт arXiv 2411.19223v5 · https://arxiv.org/pdf/2411.19223

Разложение `y_true = f*(x_true) + ε` с тремя эпистемическими членами (model approximation, measurement of y, measurement of x). Ключевое: «statements regarding 'predictability' and 'irreducibility' ... are entirely conditional on information sets»; «It is impossible to know whether we have eliminated all reducible epistemic error to approach the practical 'ceiling' of accuracy». `x_true` определён как «the best possible feature set both in terms of quantity and in quality». Сноска 2: бинарная классификация оставлена для дальнейшей работы. Допущение об отсутствии distributional shift сформулировано явно.

**Роль в проекте.** Основной вызов блоку 2. Разобран в `03-methodology/01-IDENTIFIABILITY-GATE.md`: область условная, направлена на алеаторный член относительно бесконечного универсума признаков.

## Verzelen & Gassiat — Adaptive estimation of High-Dimensional Signal-to-Noise Ratios
`[FETCHED · полный текст извлечён локально]` · Bernoulli 2018 (венью подтверждена через OpenAlex); препринт arXiv 1602.08006v2 · https://arxiv.org/abs/1602.08006

Оценка остаточной дисперсии, доли объяснённой дисперсии η и силы сигнала — эквивалентные задачи. Proposition 5.1: при p > n и любом фиксированном дизайне ранга n минимаксный риск оценки η не меньше 1/4. Theorem 4.5 и Remark 4.3: при неизвестной произвольной Σ и n^(1+ς)/p → 0 состоятельная оценка доли объяснённой вариации невозможна.

**Роль в проекте.** Проверенная теорема невозможности, задающая режим (n, p, Σ), в который нельзя заходить. Условие G3 чек-листа гейта.

## Lundberg, Brown-Weinstock, Clampet-Lundquist, Pachman, Nelson, Yang, Edin & Salganik — The origins of unpredictability in life outcome prediction tasks
`[FETCHED]` · PNAS 2024 · https://pmc.ncbi.nlm.nih.gov/articles/PMC11181083/

Задача предсказания переводится в эквивалентную задачу оценивания; ошибка раскладывается на irreducible error (внутригрупповая дисперсия среди наблюдательно идентичных единиц) и learning error. «irreducible error is a function of the task only, whereas learning error is a function of both the task and the learning approach». Три источника неустранимой ошибки: consequential intervening events, unmeasured features, imperfect measurement. Указывает, что раздельная оценка обеих компонент «is possible in at least some settings», со ссылкой на Fudenberg et al.

**Роль в проекте.** Сдвиг линии Salganik от огибающей соревнования к определению величины. Одновременно занимает часть заранее объявленного исхода C протокола.

## Fudenberg, Kleinberg, Liang & Mullainathan — Measuring the Completeness of Economic Models
`[FETCHED · препринт «Measuring the Completeness of Theories», arXiv 1910.07022, прочитан локально]` · Journal of Political Economy 2022 · https://arxiv.org/abs/1910.07022

Irreducible error определена как ожидаемая ошибка идеального правила для данного набора признаков. Completeness = отношение достигнутого снижения ошибки к достижимому. Оценщик — Table Lookup по неограниченному классу отображений с кросс-валидацией, «a consistent estimator for the irreducible error», при условии «a large number of observations for each unique feature vector x ∈ X. This requires either that the feature space X is finite...».

**Роль в проекте.** Двойная. (1) Инструмент, закрывающий гейт положительно. (2) **Серьёзный кандидат в prior art для блока 2** — оценённая доля объекта, использованная как нормировка в решении «улучшать модель на тех же признаках или искать новые признаки». Проверяется в Part C.

## Antos, Devroye & Györfi — Lower bounds for Bayes error estimation
`[МЕТАДАННЫЕ ПОДТВЕРЖДЕНЫ, СОДЕРЖАНИЕ НЕТ]` · IEEE Transactions on Pattern Analysis and Machine Intelligence 1999 · DOI 10.1109/34.777375
Заголовок, авторы, год, площадка и DOI подтверждены через OpenAlex в сессии 2026-08-18. Полный текст открыть не удалось. Приписываемое содержание (отсутствие универсальной скорости сходимости для distribution-free оценки байесовской ошибки) **не подтверждено**. Ни один вывод в волте на неё не опирается. Не цитировать до fetch.

---

# СЕССИЯ 2026-08-18 (четвёртая) — Part C, проверка новизны

> Полный разбор: `02-PRIOR-ART-VERDICT-2026-08-18.md`. Машинный свип: `01-VENUE-SWEEP-2026-08-18.md`.

## Jasberg & Sizov — The Magic Barrier Revisited: Accessing Natural Limitations of Recommender Assessment
`[FETCHED · препринт, абстракт и введение прочитаны лично]` · arXiv 2017 · https://arxiv.org/pdf/1704.05841

Оценённый из данных пол со стороны объекта плюс правило «дальше улучшать бессмысленно». Величина — тест-ретест шум целевой переменной, получаемый из повторной оценки той же единицы; к набору предикторов инвариантна.

**Роль в проекте.** Ломает трёхветвевое перечисление прежней редакции действующего утверждения. Ближайший предшественник по замыслу; путь получения величины нам закрыт по построению (фирма не проживает исход дважды).

## Said, Jain, Narr, Plumbaum — magic barrier, предшественник
`[SEARCH-SNIPPET]` · UMAP 2012 · Лично не открывалось; сведения из отчёта агента. **Не цитировать.**

## Catt — Forecastability as an Information-Theoretic Limit on Prediction
`[FETCHED · абстракт через arXiv API; полный текст НЕ прочитан, скачивание отвалилось по таймауту]` · arXiv, 28 марта 2026 · https://arxiv.org/abs/2603.27074

«Predictive loss decomposes into an irreducible component fixed by the information structure and an approximation component attributable to the method; their ratio defines the exploitation ratio, a normalised diagnostic for method adequacy.» Разложение относительно «declared information set», применённое к решению, стоит ли моделировать.

**Роль в проекте.** Угроза приоритета, не prior art: эмпирической процедуры оценивания в абстракте нет. **Прочитать полный текст до любого письма.**

## Cortes-Gomez, Dulce Rubio, Patino & Wilder — The Limits of AI-Driven Allocation: Optimal Screening under Aleatoric Uncertainty
`[FETCHED · абстракт через arXiv API]` · arXiv, май 2026 · https://arxiv.org/abs/2605.07979 · список авторов из отчёта агента, `[SEARCH-SNIPPET]`

Критерий распределения ресурса, в котором неустранимая алеаторная неопределённость стоит явно и ведёт решение. Из данных не оценивается.

## Ihlamur — When Career Data Runs Out: Structured Feature Engineering and Signal Limits for Founder Success Prediction
`[FETCHED · абстракт через arXiv API]` · arXiv, апрель 2026 · https://arxiv.org/abs/2604.00339 · фамилия автора из отчёта агента, `[SEARCH-SNIPPET]`

Предсказание успеха стартапа по карьерным данным основателей. «The signal is weak, the labels are rare (9%), and most founders who succeed look almost identical to those who fail». Признаки из прозы через LLM «capture 26.4% of model importance but add zero CV signal».

**Роль в проекте.** Ближайшая работа по предметной области, четыре месяца. Плато по исчерпанию, не оценка неустранимой доли. Эмпирическая поддержка условия G3 гейта.

## Линия декомпозиции дисперсии прибыльности — уровень OPENALEX-ABSTRACT

Для всех перечисленных подтверждены заголовок, год, площадка, авторы и текст аннотации через OpenAlex. **Полные тексты не читались.** Пометка уровня: `[OPENALEX-ABSTRACT]` — сильнее, чем `[SEARCH-SNIPPET]`, слабее, чем `[FETCHED]`.

- Rumelt, SMJ 1991 — «How much does industry matter?»
- McGahan & Porter, SMJ 1997 — «How much does industry matter, really?»
- Fitza, SMJ — CEO-эффект и случайность. **Год расходится: OpenAlex 2013, RePEc по отчёту агента 2014 (онлайн ноябрь 2013).**
- Fitza, Matusik & Mosakowski, SMJ — «Do VCs matter?». **Год расходится: OpenAlex 2008, RePEc по отчёту агента 2009.**
- Avnimelech, Dushnitsky & Ellsaesser, SMJ 2024 — акселераторы, байесовская иерархическая декомпозиция
- Mokhtar, Knockaert & Vanacker, SMJ 2026 — академические спин-оффы
- Sharapov, Kattuman & Rodríguez, SMJ 2020 — Shapley-подход; зависимость оценок от спецификации
- Bou & Satorra, SMJ 2007 — постоянная и переходная компоненты
- Brush & Bromiley, SMJ 1997; Ruefli & Wiggins, SMJ 2003; Andrews, Fainshmidt & Fitza, SMJ 2023
- Henderson, Raynor & Ahmed, SMJ 2011 — «How long must a firm be great to rule out chance?»
- Denrell, Management Science 2004 — «Random Walks and Sustained Competitive Advantage»

Через отчёты агентов, `[SEARCH-SNIPPET]`, лично не проверялось: Wang & Coff (ретроспектива линии, Strategic Management Review), Quigley & Graffin SMJ 2017 (оспаривание Fitza), Vanneste 2017 (мета-анализ), Misangyi et al. 2006, Bowman & Helfat 2001, Powell SMJ 1996, Roquebert/Phillips/Westfall SMJ 1996.

## Schmalensee — Do Markets Differ Much?
`[CITATION-ONLY]` · American Economic Review 1985 · Подтверждён только ссылкой внутри проверенной аннотации Rumelt 1991. Ни OpenAlex, ни Crossref запись не разрешили. **Не цитировать.**

## Смежное, проверено на уровне аннотации OpenAlex
- Oparina et al., Scientific Reports 2025 — «establish an upper bound on the predictability of wellbeing scores with survey data». Оценённый потолок социального исхода, решения о развёртывании нет.
- Verhagen, Socius 2022 — «A Pragmatist's Guide to Using Prediction in the Social Sciences». Потолка не оценивает.
- Qu, Kumar & Tong, Strategy Science 2026 — предсказания в решениях о поглощениях. Аргумент в пользу инвестиций в предсказание, потолка нет.
- Farmer & Lafond, Research Policy 2016 — распределение ошибок прогноза как функция горизонта, проверено хиндкастингом. Модельная граница при предположенном случайном блуждании.

---

# СЕССИЯ 2026-08-18 (пятая) — Catt, ILD, DataEval, Avnimelech

## Catt — Forecastability as an Information-Theoretic Limit on Prediction
`[FETCHED · ПОЛНЫЙ ТЕКСТ, три маршрута: HTML arXiv, ar5iv, PDF]` · arXiv, 28 марта 2026 · https://arxiv.org/abs/2603.27074
Прежняя запись `[FETCHED · только абстракт]` заменена. Разбор: `02-CATT-2026-ASSESSMENT.md`.

Постановка — процесс, индексированный временем, прогноз $Y_{t+h}$ при объявленном информационном множестве как суб-σ-алгебре. Proposition 9: ожидаемая log-потеря = условная энтропия (неустранимое) + ожидаемая KL-дивергенция (приближение). Тождество автор относит не к себе: «This identity is established in the predictability literature by DelSole [6]». Раздел VII: величина **оценивается из данных** оценщиком взаимной информации KSG, с перестановочным нулём; компаньон валидирует на более чем 42 000 рядов против out-of-sample sMAPE. Раздел VIII: «The framework is diagnostic rather than prescriptive ... does not by itself determine a forecasting model or decision rule.» Точное равенство только для log loss; «For practitioners who evaluate forecasts under squared-error loss, CRPS, or quantile loss, the exact equality proved here does not transfer.» Содержания про фирмы и организации нет.

## DelSole — Predictability and information theory. Part I: Measures of predictability
`[CITATION-ONLY]` · Journal of the Atmospheric Sciences 2004 · Источник тождества, на который ссылается Catt. Сам не открывался. **Не цитировать до fetch** — но знать, что понятию двадцать два года.

## Catt — компаньон, эмпирическая работа
`[CITATION-ONLY]` · рукопись на рецензии, SSRN, 2026 · doi 10.2139/ssrn.6416626 · Не открыта. **Первоочередной след:** если там есть шаг решения, остаток блока 2 закрывается.

## ILD — A Model-Agnostic Algorithm for Bayes Error Determination in Binary Classification
`[FETCHED · полный текст]` · arXiv 2021 · https://arxiv.org/abs/2107.11609

Байесовская ошибка для бинарного исхода при категориальных признаках, без модели, через «feature buckets» — комбинации значений признаков. Авторы прямо называют решения, которые величина обслуживает: «to decide when to stop searching for better models; to decide if it is necessary to enrich the dataset». Ограничение: ячейки должны быть населены; при одном наблюдении на ячейку алгоритм бесполезен. Нерешённое: отделение достижимой точности от переобучения.

**Роль в проекте.** Двойная. Берёт глагол «улучшать» из прежней формулировки утверждения. И одновременно даёт готовый оценщик для режима, в который загоняет гейт.

## DataEval — документация функции `ber`
`[FETCHED]` · документация инструмента, версия 0.69.2 · https://dataeval.readthedocs.io/en/v0.69.2/concepts/BER.html

«The ber function assesses the feasibility of a machine learning classification task by estimating this error rate ... If this difficulty surpasses operational performance requirements, then the problem must be changed in order to become feasible.» Оценщики — kNN и минимальное остовное дерево, из линии границ на многоклассовую байесовскую ошибку.

**Уровень:** документация инструмента, не критерий в литературе. Но проверка выполнимости против операционного требования по точности сформулирована явно.

## Avnimelech, Dushnitsky & Ellsaesser — Are accelerators akin to breweries or wineries?
`[FETCHED · полный текст, репозиторий London Business School]` · Strategic Management Journal 2024 · https://lbsresearch.london.edu/id/eprint/3828/

Байесовская иерархическая декомпозиция дисперсии результативности стартапов по акселератору, менеджеру, когорте, индустрии и году. Остаток определён в модели: «The error term ε_s captures startup-specific idiosyncratic performance differences.» **В таблице результатов строки остатка нет.** Проверено лично на первичном тексте.

**Роль в проекте.** Прямое подтверждение B2: в живой линии нашей предметной области величина определяется в модели и опускается в результатах.

---

# СЕССИЯ 2026-08-18 (шестая) — компаньон Catt

## Catt — Horizon-resolved Forecastability of Time Series via Auto Mutual Information
`[FETCHED · ПОЛНЫЕ ТЕКСТЫ ДВУХ ВЕРСИЙ]` · arXiv `2601.10006`, v1 январь 2026, v5 август 2026 · https://arxiv.org/abs/2601.10006

Эмпирический компаньон к теоретической работе `2603.27074`. Отождествление с SSRN-записью 10.2139/ssrn.6416626 — **вывод по совпадению содержания, не подтверждённый факт**: SSRN закрыт Cloudflare и лично не открывался; аннотация SSRN получена через Crossref и совпадает с версиями v1–v4 по объёму данных (42 355 рядов, шесть частот) и метрике (sMAPE). Заголовки разные.

v4: триаж рядов по терцилям AMI на категории действия «invest in modelling / model cautiously / manage uncertainty»; раздел «Implications for Decision Workflows»; gating rule по многомерному обогащению. Ни цен ошибок, ни базовой ставки. v5: рескоуп на M4 Monthly под официальный holdout, связь заметно слабее, слой решения вынесен в future work — «developing and evaluating such decision layers is future work». Ключевое ограничение самого автора: «high AMI evidences recoverable structure, whereas low AMI does not establish its absence».

**Роль в проекте.** Оставляет зазор открытым. Разбор: `03-CATT-COMPANION-ASSESSMENT.md`.

## Catt — On the Limits of Prediction: Forecastability Profiles and Information Decay in Time Series
`[МЕТАДАННЫЕ ЧЕРЕЗ arXiv API]` · arXiv `2603.20546` · Предшественник теоретической работы, снят самим автором: «Resubmitted as a highly revised paper — [arXiv:2603.27074]». Отдельной ценности не имеет.

## SSRN 10.2139/ssrn.6416626 — аннотация
`[FETCHED через Crossref API]` · https://api.crossref.org/works/10.2139/ssrn.6416626 · Полный текст НЕ открыт: SSRN закрыт Cloudflare, DOI отдаёт 403. Аннотация подтверждена дословно.

---

# СЕССИЯ 2026-08-20 (восьмая) — занятость границы `G ≤ σ/2`

## Cover & Hart 1967 — Nearest Neighbor Pattern Classification
`[FETCHED · ПОЛНЫЙ ТЕКСТ]` · IEEE Transactions on Information Theory 13(1):21–27 · https://isl.stanford.edu/~cover/papers/transIT/0021cove.pdf

Подтверждено дословно: ур. (25) `R = 2R*(1 − R*) − 2 Var r*(x)`, ур. (26) `R ≤ 2R*(1 − R*)`, «with equality iff `Var r* = 0`». Здесь `r*(x) = min(η, 1−η)`.

**Роль в проекте.** Симметричный частный случай (`π = a = ½`) нашей границы `G ≤ σ/2` — это ровно ур. (26) после перестановки. Одна из линий занятости. Разбор: `06-BOUND-PRIOR-ART-2026-08-20.md`.

## Scarf 1958 — A Min-Max Solution of an Inventory Problem
`[ATTRIBUTED-THROUGH-FETCHED]` · существование и метаданные по OpenAlex (`W2558813012`, `W431821928`); **оригинал НЕ открывался**.

Формулировка неравенства взята из прочитанного независимого источника, который её приводит и атрибутирует Скарфу: `E(X−q)⁺ ≤ [μ−q+√((μ−q)²+σ²)]/2`. **Цитировать оригинал дословно нельзя.** Для вывода о занятости достаточно: неравенство приводится и используется как общеизвестное.

**Роль в проекте.** Главная линия занятости границы `G ≤ σ/2`: наша граница — значение правой части при `q = π`, а опубликованная форма острее.

## Li & Prokhorov — Improved Semi-Parametric Bounds for Tail Probability and Expected Loss
`[FETCHED · ПОЛНЫЙ ТЕКСТ HTML]` · arXiv `2404.02400v3`, econ.EM, май 2025 · https://arxiv.org/html/2404.02400v3

Источник формулировки неравенства Скарфа и его контекста («Scarf's inequality is a well-known bound on linear expected loss»), а также перечня применений: ценообразование опционов `[REF: Lo 1987]`, страхование, управление запасами.

## Gail & Pfeiffer 2009 — Measures to Summarize and Compare the Predictive Capacity of Markers
`[FETCHED · ПОЛНЫЙ ТЕКСТ]` · https://pmc.ncbi.nlm.nih.gov/articles/PMC2827895/

Подтверждено дословно: `TG = ∫₀¹ |R(ν) − ρ| dν` с атрибуцией Bura & Gastwirth 2001; `PEV = var(risk(Y))/ρ(1−ρ)`; тождество `TG = 2ρ(1−ρ){TPR(ρ) − FPR(ρ)} = 2ρ(1−ρ)·supₜ{ROC(t) − t}` и то, что максимум `TPR(p) − FPR(p)` достигается при `p = ρ`.

**Роль в проекте.** `2·G(π) = TG`, `1 − B = PEV`. Обе наши величины названы здесь как стандартные меры и стоят соседними разделами.

## Bura & Gastwirth 2001 — The Binary Regression Quantile Plot
`[ATTRIBUTED-THROUGH-FETCHED]` · Biometrical Journal · метаданные по OpenAlex (`W2112446629`); **оригинал НЕ открывался**. Определение Total Gain и граница `TG ≤ 2ρ(1−ρ)` подтверждены через два независимых прочитанных источника (`PMC2827895`, `PMC4486698`). Цитировать дословно нельзя.

## Choodari-Oskooei, Royston & Parmar 2015 — The Extension of Total Gain (TG) Statistic in Survival Models
`[FETCHED · ПОЛНЫЙ ТЕКСТ]` · BMC Med Res Methodol 15:50 · https://pmc.ncbi.nlm.nih.gov/articles/PMC4486698/

Подтверждено дословно: `TG = ∫₀¹ |R(υ) − π₀| dυ`, `TG_STD = TG/(2π₀(1−π₀))`, и прямое сопоставление L1-версии (TG, «mean absolute deviation») с L2-версией (`R²_Pepe`, «mean squared deviation»).

## Reid & Williamson 2009 — Information, Divergence and Risk for Binary Experiments
`[FETCHED · ПОЛНЫЙ ТЕКСТ]` · arXiv `0901.0356` · https://ar5iv.labs.arxiv.org/html/0901.0356

**Повышение уровня провенанса:** в прошлой сессии работа бралась только по абстракту (PDF отваливался по таймауту дважды, ar5iv и HTML не отвечали). 2026-08-20 ar5iv отдал полный текст.

Подтверждено дословно: статистическая информация `ΔL̲(η,M) = L̲(π,M) − L̲(η,M)`, введена DeGroot 1962, выражается как «concave Jensen gap»; примитивы всей конструкции «all are related to cost-sensitive binary classification».

**Отрицательный результат, важный для протокола:** моментной границы там нет. «Scarf» не встречается, «variance» встречается пять раз и не в роли границы; выводимые границы — суррогатные и пинскеровского типа через вариационную дивергенцию.

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

# СТАТУС УТВЕРЖДЕНИЯ ПОСЛЕ B1 И B2

> Сессия 2026-08-18, часть B. Продолжение `02-PRIOR-ART-VERDICT-2026-08-18.md` и `02-CATT-2026-ASSESSMENT.md`.

---

# B1. Оценка байесовской ошибки как проверка выполнимости — открыто, и утверждение приходится сузить третий раз

Прошлая сессия назвала это «структурно самым опасным объектом, который кто-либо нашёл», и никто его не открывал. Открыто.

## Что там оказалось

**Документация DataEval, функция `ber`** `[FETCH: https://dataeval.readthedocs.io/en/v0.69.2/concepts/BER.html · 2026-08-18]`:

> «Bayes error rate refers to the irreducible error in a particular classification problem. The ber function assesses the feasibility of a machine learning classification task by estimating this error rate.»

> «The ber metric should be used when you would like to measure the feasibility of a machine learning classification task. For example, you would like to know if the operational accuracy requirement of 80% is achievable given the imagery.»

> «This quantity is of interest because it informs an engineer about the inherent difficulty of a problem. If this difficulty surpasses operational performance requirements, then the problem must be changed in order to become feasible.»

Оценщики — k ближайших соседей и минимальное остовное дерево, со ссылкой на линию «Learning to Bound the Multi-class Bayes Error», то есть **границы**, а не точечная доля.

**И то, чего прошлая сессия не видела вовсе:** `[REF: ILD 2021]`, «A Model-Agnostic Algorithm for Bayes Error Determination in Binary Classification», arXiv, полный текст прочитан `[FETCH: https://arxiv.org/pdf/2107.11609 · 2026-08-18]`.

Это алгоритм определения байесовской ошибки для **бинарного исхода при категориальных признаках** — ровно тот режим, в который гейт нас загоняет. Из абстракта: «determine the best possible performance, measured in terms of the AUC ... and accuracy, that can be obtained from a specific dataset in a binary classification problem with categorical features *regardless* of the model used».

И — решающее — авторы прямо перечисляют решения, которые их величина обслуживает:

> «The ILD algorithm is of fundamental importance to practitioners because it allows: • to determine the prediction power (namely, the BE) of a specific set of categorical features; • **to decide when to stop searching for better models**; • **to decide if it is necessary to enrich the dataset.**»

## Берёт ли это уцелевшее утверждение

**Да, в той формулировке, которую я написал в конце прошлой сессии. Берёт.**

Та формулировка звучала: «ни один опубликованный критерий принятия решения о том, **строить, улучшать** или разворачивать предсказательную систему, не включает полученную из данных оценку доли ошибки, неустранимой при обусловливании на объявленном наборе признаков».

ILD: оценка из данных — есть; обусловливание на объявленном наборе признаков (категориальные признаки) — есть; решение об **улучшении** («when to stop searching for better models») и о сборе данных («if it is necessary to enrich the dataset») — заявлено авторами прямым текстом. Глагол «улучшать» из утверждения надо убрать, иначе утверждение ложно.

## Что остаётся после третьего сужения

> Ни один опубликованный критерий не связывает полученную из данных оценку неустранимой доли **с решением о развёртывании, взвешивающим цены ошибок двух родов против базовой ставки исхода**. Оценённые полы, которые существуют, обслуживают либо «когда прекращать настройку» (magic barrier, ILD), либо «достижимо ли операционное требование по точности» (DataEval), либо «где по горизонтам окупается моделирование» (Catt). Ни один не сравнивает с решением без модели, ни один не содержит порога, чистой выгоды или асимметрии цены ошибок.

**Это третье сужение за две сессии, и это надо назвать прямо.** Ход «оценить пол и решить, продолжать ли» заселён минимум в трёх местах. Незанятым остаётся **один** ход: связка оценённого пола с теоретико-решающим аппаратом развёртывания. Мой честный прогноз: это тонко, но не пусто — область параметров, в которой знание пола переворачивает вердикт net benefit при низкой базовой ставке, есть настоящий аналитический объект. Но рамка «мы вводим мысль, что часть ошибки неустранима» ушла полностью, и работа должна писаться как «дан оценённый пол — вот когда именно вердикт развёртывания переворачивается», а не как введение величины.

## Побочно: B1 дал инструмент, а не только угрозу

ILD работает ровно в нашем режиме — бинарный исход, категориальные признаки — и его ограничение слово в слово совпадает с условием G2 гейта:

> «the ILD algorithm works well when the different buckets are populated with enough observations. The ILD algorithm would not give any useful information on a dataset with just one observation in each bucket (since it would be a perfect dataset).»

И честная оговорка авторов в приложении:

> «there is a big assumption made, namely, that a feature bucket with a few observations contains the same information as one with one thousand observations in it»

Плюс нерешённая ими проблема: отделить достижимую точность от переобучения («how to determine the maximum accuracy or the best AUC only in cases in which no overfitting is occurring ... currently under investigation by the authors»).

**Занести в гейт:** «feature bucket» ILD — это ровно ковариатная ячейка условий G1–G2. Четвёртое независимое подтверждение размерностной стены.

---

# B2. Примирение «блок 2 — не открытая территория» с «отрицательный результат держится»

Прошлая сессия написала обе фразы, и они выглядят противоречащими. Не противоречат, но различие надо провести точно, потому что оно и есть остаток вклада.

## Что эти работы оценивают

Проверено на самой свежей работе линии в нашей области, прочитанной лично: `[REF: Avnimelech, Dushnitsky & Ellsaesser 2024]`, SMJ `[FETCH: https://lbsresearch.london.edu/id/eprint/3828/1/ · 2026-08-18]`.

Оценивается **доля общей дисперсии реализованного исхода, относимая к именованным эффектам принадлежности**. Модель — байесовская иерархическая со случайными пересечениями для акселератора, менеджера, когорты и индустрии, фиксированным эффектом года и контролем на предыдущее финансирование. Из текста: «The table reports the mean percentages of the total variance in startup fundraising after entering an accelerator which is explained by each effect.»

Это дисперсия исхода, не дисперсия ошибки предсказания.

## Сообщает ли кто-нибудь остаток

**Нет. И это проверено мной прямо, а не через пересказ.**

Остаток в модели определён: «The error term ε_s captures startup-specific idiosyncratic performance differences.» То есть величина в модели названа, и названа именно как идиосинкразия стартапа.

**В таблицу результатов она не попадает.** Table 3 имеет строки: Accelerator, Manager, Cohort, Industry, Year, Pre accelerator funding. **Строки остатка нет.** Названные компоненты в полной модели покрывают заметно меньшую часть общей дисперсии, чем оставляют неотнесённой, и эта неотнесённая часть не сообщается, не называется и не интерпретируется нигде в разделе результатов.

Это тот же рисунок, который прошлая сессия получила для сводной таблицы ретроспективы линии (нет колонки остатка, ноль вхождений «residual», «unexplained», «irreducible», «noise») — но там это был пересказ агента, а здесь проверено на первичном тексте самой свежей работы в нашей предметной области.

Отдельно стоит отметить, что out-of-sample аппарат в работе **есть** — leave-one-out кросс-валидация и апостериорные предсказательные проверки, — но применяется он к проверке качества подгонки модели, а не к оценке потолка.

## Что именно остаётся незанятым — предложение, которое надо оставить как есть

> В области фирм и стартапов величина никогда не сообщается: линия декомпозиции дисперсии оценивает именованные эффекты принадлежности и печатает их, а остаток определяет в модели и опускает в результатах. В области ML и инструментов величина сообщается и привязывается к решениям «прекращать ли настройку» и «достижимо ли требование по точности», но никогда — к вердикту развёртывания с ценами ошибок и базовой ставкой. Незанят ровно стык этих двух: сообщить величину для фирменного исхода и довести её до решения о развёртывании.

Это узко. Это правда. Расширять это предложение нельзя.

## Следствие для формулировки блока 2

«Декомпозиция дисперсии результативности стартапов» как описание блока 2 **запрещена** — это занятая машинерия, SMJ 2009, 2024, 2026, плюс работа на данных GALI 2020, которую цитирует Avnimelech. Описание блока 2 должно называть величину и решение, а не метод.

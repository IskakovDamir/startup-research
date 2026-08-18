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

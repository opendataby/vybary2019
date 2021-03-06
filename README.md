Информация о кандидатах в пригодном для анализа виде. По всем вопросам:

  * Telegram: https://t.me/opendataby

Существует три независимо собранных датасета:

1. https://github.com/ushchent/el_machina/ - продолжение проекта
"[Избирательная машина](https://github.com/opendataby/elect_machine)" 2016 года
(@chegor, @gsk990, @ushchent и др.) с обновлёнными данными на 2019 для
предсказания результатов. Среди прочего содержит астральные знаки зодиака
для более чёткого прочтения знаков вселенной.

2. [excel](excel) - датасет от Dmitry Rogozhny (@dmitryrogozhny) -
ламповый датасет в формате Excel и CSV с информацией о том, кто из
кандидатов уже является депутатом.

3. [dataset](dataset) - полностью автоматический парсинг сайта http://vybary2019.by
на Python + pandas. Есть задача кроме парсинга таблиц, ещё парсить текст, в котором
упоминаются доходы, даты рождения и, возможно, другая полезная для анализа информация.


### Обновление датасета 3

Для обновления dataset/regions.csv нужен только Python 3.
```
python3 01pages.py -f
```
Для обновления dataset/candidates.csv нужен как минимум [Jupyter](https://jupyter.org/).
```
jupyter nbconvert --execute parse.ipynb
```


### Введение в pandas :D

Распарсить HTML страницу, сохранить первую табличку в `pandas` dataframe `d`.
Добавить пробел в восьмую позицию в каждой строке первой колонке, потому что
`pandas` его склеивает
https://github.com/pandas-dev/pandas/issues/29528

```python
import pandas as pd
d = pd.read_html('http://vybary2019.by/regions/49.html',header=0)[0]
d.iloc[:,0] = d.iloc[:,0].apply(lambda x: x[:8]+' '+x[8:])
```


### ChangeLog

2019.11.17 (дзень выбарау)

- -1 кандидат в Гомеле по 32му региону, всего участвует 518
- в [сравнение датасетов](canal02-datadiff.ipynb) добавлен датасет
  `el_machina`, размеры датасетов, сравенения полей

2019.11.16 (завтра)

- конкурс от am@opendata.by (@ushchent) - до сегодняшнего вечера нужно
  прислать PR со своими вариантами - кто пройдёт и кто нет из кандидатов
  2019го года в CSV на https://github.com/ushchent/el_machina
  Формат, допустим `data/predict-{user}.csv`, присутствовать должны
  только кандидаты 2019го, как минимум идентификатор кандидата и булевый
  флаг прошёл/или нет. Вероятность желательна, но необязательна.

2019.11.15 (2 дня до выборов)

- надо попуститься

2019.11.14 (за 3 дня)

- dataset/regions.csv готов, вместе с границами и контактами
- добавлены тетрадки с экспериментами
  - `canal02-datadiff.ipynb` - незаконченное сравнение датасетов
  - `canal03-parsing.ipynb` - задача извлечения значений с помощью ML
  - `canal03-parsing-with-mindsdb.ipynb` - фейл извлечения с помощью MindsDB

2019.11.13 (4)

- за два дня с 10:39 11го ноября выбыло 5 кандидатов
- инструкции по обновлению датасета
- CSV с кандидатами уехала в dataset/candidates.csv
- [canal01-generations.ipynb](canal01-generations.ipynb) - анализ поколений кандидатов
- заработали предсказания на 2019ый http://ushchent.github.io/el_machina/

2019.11.12 (осталось 5)

- описание всех трёх датасетов
- ссылка на проект предсказания выборов от Alexey Medvetsky
- экспорт распаршеных кандидатов в CSV (@Alexanderexe)

2019.11.11 (6 дней до..)

- независимо собранный excel от @dmitryrogozhny с доп.информацией - пол и является ли
  текущим депутатом
- скрипт `./go.sh` для сборки датасета
- собранные скриптами данные теперь в [`,/dataset`](dataset) (пока только [`regions.csv`](dataset/regions.csv))

2019.11.10 (за 7 дней до..)

- проект на гитхабе, maintenance команд на гитхаб и настройка команды @opendata/datafolks
- иконка @opendata/datafolks из случайного скриншота
- тикет в пандас https://github.com/pandas-dev/pandas/issues/29528
- `parse.ipynb` парсинг данных кандидата на pandas + BeautifulSoup (@Alexanderexe)
- `dataset/regions.csv` спиcок регионов с сайта (@abitrolly)

### Credits

* @Alexanderexe
* @abitrolly
* @dmitryrogozhny
* @ushchent
* @chego
* @gsk990
* и др.

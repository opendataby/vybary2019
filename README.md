Информация с http://vybary2019.by в пригодном для саентизма виде.

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

### План

* [ ] таблица кандидаты
* [x] таблица регионы
* [ ] всё остальное

### ChangeLog

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

@Alexanderexe
@abitrolly
@dmitryrogozhny

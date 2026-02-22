# Проект epidemiological_data
Файл *`main.py`* - бекенд на python, принимет в режиме около реального времени с задаваемой частотой дискретизации. Чтобы запустить, нужно использовать файл *`run.py`*

```python
python run.py
```

После этого можно будет зайти через браузер на такие адреса: 
```text
Документация API: http://localhost:8000/docs
Альтернативная документация: http://localhost:8000/redoc
Главная страница: http://localhost:8000/
```

Папка *`datasets`* содержит датасеты, связанные с эпидемиологией (частоты заболеваемости за период и гео-метки) 

Файл *`plotly_test.py`* - график с географическими координатами из файла COVID-19 in Italy province

## Источники датасетов и их описание

1. Novel Corona Virus 2019 Dataset -
https://www.kaggle.com/datasets/sudalairajkumar/novel-corona-virus-2019-dataset

Источник: Johns Hopkins University Center for Systems Science and Engineering CSSE
```text
Данные представляют собой ежедневную статистику по провинциям/штатам и странам мира.

SNo | Порядковый номер записи в таблице.
ObservationDate | Дата, за которую собрана статистика.
Province/State | Название провинции, штата или территории внутри страны.
Country/Region | Название страны или региона.
Last Update | Временная метка последнего обновления данных для данной строки.
Confirmed | Суммарное количество подтверждённых случаев COVID-19 в указанном регионе на дату наблюдения.
Deaths | Суммарное количество летальных исходов, связанных с COVID-19, в указанном регионе на дату наблюдения.
Recovered | Суммарное количество выздоровевших пациентов в указанном регионе на дату наблюдения.
```
2. Novel Corona Virus Disease in India -
https://www.kaggle.com/datasets/sudalairajkumar/covid19-in-india

Источник: Ministry of Health & Family Welfare, правительство Индии
```text
Данные представляют собой ежедневную сводку по штатам и союзным территориям Индии с накопительными показателями.

Sno | Порядковый номер записи.
Date | Дата отчёта.
Time | Время отчёта.
State/UnionTerritory | Название штата или союзной территории.
ConfirmedIndianNational | Суммарное число подтверждённых случаев среди граждан Индии на указанную дату.
ConfirmedForeignNational | Суммарное число подтверждённых случаев среди иностранных граждан на указанную дату.
Cured | Суммарное число выздоровевших на указанную дату.
Deaths | Суммарное число умерших на указанную дату.
Confirmed | Общее суммарное число подтверждённых случаев.
```

3. COVID-19 in South Korea -
https://www.kaggle.com/datasets/kimjihoo/coronavirusdataset

Источник: Johns Hopkins University Center for Systems Science and Engineering CSSE
```text
Данные содержат сведения о кластерах заражений COVID-19 в Южной Корее, сгруппированные по провинциям, городам и источникам заражения.Источник: Johns Hopkins University Center for Systems Science and Engineering CSSE

case_id | Уникальный идентификатор записи.
province | Название провинции или города-метрополии.
city | Конкретный город или район внутри провинции, где произошла вспышка.
group | Логическое значение. TRUE – запись описывает кластер. FALSE – запись относится к общим категориям.
infection_case | Описание конкретной вспышки или источника заражения.
confirmed | Количество подтверждённых случаев, связанных с данной записью.
latitude | Широта места, связанного со вспышкой.
longitude | Долгота места, связанного со вспышкой.
```
4. COVID-19 in Italy province -
https://www.kaggle.com/datasets/sudalairajkumar/covid19-in-italy

Источник: Dipartimento della Protezione Civile, Италия
```text
Данные представляют собой детализированную информацию о распространении COVID-19 на уровне отдельных провинций Италии. Они сочетают в себе административное деление, географические координаты и ежедневную статистику.

SNo | Порядковый номер записи в таблице.
Date | Дата и время сбора статистики.
Country | Трёхбуквенный код страны.
RegionCode | Уникальный числовой код региона Италии.
RegionName | Название региона Италии.
ProvinceCode | Уникальный числовой код провинции.
ProvinceName | Название провинции.
ProvinceAbbreviation | Двухбуквенное сокращение провинции.
Latitude | Географическая широта административного центра провинции.
Longitude | Географическая долгота административного центра провинции.
TotalPositiveCases | Общее количество положительных случаев COVID-19, зарегистрированных в данной провинции на указанную дату.
```

5. Coronavirus - Brazil -
https://www.kaggle.com/datasets/unanimad/corona-virus-brazil

Источник: Sistema Único de Saúde SUS, правительственные порталы Бразилии
```text
Данные содержат информацию о муниципалитетах Бразилии, включая их географическое положение и статус столицы штата. 

state_code | Двузначный код штата.
city_code | Уникальный семизначный код муниципалитета.
city_name | Название города.
lat | Географическая широта центра города в десятичных градусах.
long | Географическая долгота центра города в десятичных градусах.
capital | Логическое значение, указывающее, является ли город столицей своего штата.
```

6. Zika Virus Epidemic -
https://www.kaggle.com/datasets/cdc/zika-virus-epidemic?resource=download

Источник: Centers for Disease Control and Prevention CDC
```text
Это эпидемиологические данные о распространении вируса Зика в Аргентине. 

report_date | Дата отчёта.
location | Уникальный идентификатор местоположения, состоящий из названия страны и региона.
location_type | Тип административной единицы, к которой относится запись.
data_field | Описание типа данных, представленных в строке.
data_field_code | Уникальный код, соответствующий типу данных.
time_period | Временной период, за который собран показатель.
time_period_type | Тип временного периода.
value | Числовое значение показателя.
unit | Единица измерения показателя.
```

7. Italian COVID-19 regional dataset -
https://www.kaggle.com/datasets/alessandrabilardi/italian-covid-19-region-dataset/

Источник: Министерство здравоохранения Италии и региональные органы здравоохранения 
```text
Данные представляют собой детализированную ежедневную статистику по регионам Италии, включая как абсолютные показатели, так и их нормализованные версии. 

date | Дата и время сбора статистики.
state | Код страны.
region_code | Уникальный числовой код региона Италии.
region_name | Название региона Италии.
lat | Географическая широта административного центра региона.
long | Географическая долгота административного центра региона.
hospitalized_with_symptoms | Количество пациентов, госпитализированных с симптомами COVID-19.
intensive_care | Количество пациентов в отделениях интенсивной терапии.
total_hospitalized | Общее количество госпитализированных пациентов.
home_isolation | Количество пациентов, находящихся на домашнем карантине.
total_positives | Общее количество активных положительных случаев на текущую дату.
new_positives | Количество новых положительных случаев, выявленных за последние сутки.
intensive_care_admissions | Количество новых поступлений в отделения интенсивной терапии за последние сутки.
discharged_recovered | Суммарное количество выписанных и выздоровевших за всё время пандемии.
deceased | Суммарное количество умерших за всё время пандемии.
total_cases | Общее количество подтверждённых случаев с начала пандемии.
daily_discharged_recovered | Количество выписанных/выздоровевших за последние сутки.
daily_deceased | Количество умерших за последние сутки.
daily_total_cases | Количество новых подтверждённых случаев за последние сутки.
hospitalized_with_symptoms_normalized_per_region_name | Нормализованное значение hospitalized_with_symptoms.
intensive_care_normalized_per_region_name | Нормализованное значение intensive_care.
total_hospitalized_normalized_per_region_name | Нормализованное значение total_hospitalized.
home_isolation_normalized_per_region_name | Нормализованное значение home_isolation.
total_positives_normalized_per_region_name | Нормализованное значение total_positives.
new_positives_normalized_per_region_name | Нормализованное значение new_positives.
intensive_care_admissions_normalized_per_region_name | Нормализованное значение intensive_care_admissions.
daily_discharged_recovered_normalized_per_region_name | Нормализованное значение daily_discharged_recovered.
daily_deceased_normalized_per_region_name | Нормализованное значение daily_deceased.
daily_total_cases_normalized_per_region_name | Нормализованное значение daily_total_cases.
```

8. Climate-Driven Disease Spread -
https://www.kaggle.com/datasets/hopeofchange/climate-driven-disease-spread

Источник: Всемирная организация здравоохранения WHO и национальные метеорологические службы. 
```text
Данные представляют собой многолетние помесячные данные по Палестинской территории, объединяющие климатические показатели, индексы окружающей среды и статистику по инфекционным заболеваниям. 

year | Год наблюдения.
month | Месяц наблюдения.
country | Название страны.
region | Название региона внутри страны.
avg_temp_c | Среднемесячная температура воздуха в градусах Цельсия.
precipitation_mm | Суммарное количество осадков за месяц в миллиметрах.
air_quality_index | Индекс качества воздуха.
uv_index | Индекс ультрафиолетового излучения.
malaria_cases | Количество зарегистрированных случаев малярии за месяц.
dengue_cases | Количество зарегистрированных случаев лихорадки денге за месяц.
population_density | Плотность населения.
healthcare_budget | Бюджет на здравоохранение.
```

9. COVID-19 useful features by country -
https://www.kaggle.com/datasets/ishivinal/covid19-useful-features-by-country

Источник: Our World in Data OWID и Всемирный банк.
```text
Данные представляют собой статические характеристики стран, полезные для анализа факторов, влияющих на распространение COVID-19 (например, демография, туризм, даты введения ограничений).  

Country_Region | Название страны или региона.
Population_Size | Численность населения.
Tourism | Количество туристов (годовой поток или индустриальный показатель).
Date_FirstFatality | Дата первой зарегистрированной смерти от COVID-19 в стране.
Date_FirstConfirmedCase | Дата первого подтверждённого случая COVID-19 в стране.
Latitude | Географическая широта центральной точки страны.
Longtitude | Географическая долгота центральной точки страны.
Mean_Age | Средний возраст населения страны.
Lockdown_Date | Дата введения режима изоляции.
Lockdown_Type | Тип введённого локдауна: Full (полный) или Partial (частичный).
Country_Code | Трёхбуквенный код страны.
```

10. COVID-19 Global Impact Tracker -
https://www.kaggle.com/datasets/shreyasur965/covid-19-global-impact-tracker

Источник: Our World in Data OWID и международные статистические организации. 
```text
Данные представляют собой итоговую статистику по пандемии COVID-19 для большого количества стран и территорий.

country | Название страны или территории.
code | Двухбуквенный код страны.
confirmed | Общее количество подтверждённых случаев COVID-19 за всё время пандемии.
recovered | Общее количество выздоровевших пациентов за всё время пандемии.
critical | Количество пациентов в тяжёлом или критическом состоянии на момент последнего обновления.
deaths | Общее количество летальных исходов, связанных с COVID-19, за всё время пандемии.
lastChange | Дата и время последнего изменения данных по этой стране.
lastUpdate | Дата и время последнего обновления данных по этой стране.
latitude | Географическая широта страны.
longitude | Географическая долгота страны.
```

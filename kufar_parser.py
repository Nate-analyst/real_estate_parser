import pandas as pd

from Page_counter import page_counter
from Raw_data_parser import raw_data_parser
from Data_filter import data_filter
from Final_processing import final_processing

amount_of_pages = page_counter()
print(f"Количество страниц для парсинга: {amount_of_pages}")

all_ads = raw_data_parser(amount_of_pages)

parameters = ['Микрорайон', 'Комнат', 'Цена за м²', 'Общая площадь', 'Жилая площадь', 'Площадь кухни', 'Санузел', 'Высота потолков','Ремонт', 
              'Этаж', 'Этажность дома', 'Материал стен', 'Год постройки', 'В новостройке', 'Состояние', 'Область', 'Город / Район','Метро', 
              'Жилой комплекс', 'Координаты']

filtered_ads = data_filter(all_ads, parameters)

ads_df = final_processing(filtered_ads)

print("Данные сохранены в файл: all_ads.xlsx")
ads_df.to_excel('all_ads.xlsx', index=False)

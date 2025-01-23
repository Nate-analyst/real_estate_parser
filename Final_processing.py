import pandas as pd

def final_processing(filtered_ads):

    field_mapping = {
        'Категория': 'vl',
        'Цена за м²': 'v',
        'Комнат': 'vl',
        'Общая площадь': 'v',
        'Жилая площадь':'v',
        'Площадь кухни':'v',
        'Балкон':'vl',
        'Санузел':'vl',
        'Есть проходная комната':'vl',
        'Высота потолков':'vl',
        'Ремонт':'vl',
        'Этаж': 'v',
        'Не первый этаж':'vl',
        'Не последний этаж':'vl',
        'Этажность дома':'v',
        'Материал стен':'vl',
        'Год постройки':'v',
        'В новостройке':'vl',
        'Окна выходят':'vl',
        'Обустройство дома':'vl',
        'Через аукцион/конкурс':'vl',
        'Состояние':'vl',
        'Возможен обмен':'vl',
        'Область':'vl',
        'Город / Район':'vl',
        'Метро':'vl',
        'Жилой комплекс':'vl',
        'Координаты':'v',
        'Микрорайон': 'vl'
    }

    results = []

    for ad in filtered_ads:

        ad_result = {
            'ad_id': ad['ad_id'],
            'ad_link': ad['ad_link'],
            'price_byn': ad['price_byn'],
            'price_usd': ad['price_usd'],
            'company_ad':ad['company_ad']
        }
        
        for item in ad['filtered_parameters']:
            param_name = item['pl']
            if param_name in field_mapping:
                value_field = field_mapping[param_name]
                value = item.get(value_field)
                ad_result[param_name] = value
                if value == None:
                    ad_result[param_name] = None
        
        results.append(ad_result)

    ads_df = pd.DataFrame(results)
    print(f'''There are exactly {len(ads_df)} ads and {ads_df['ad_id'].duplicated().sum()} duplicated ads.''')

    ads_df['Широта'] = ads_df['Координаты'].str[1]
    ads_df['Долгота'] = ads_df['Координаты'].str[0]

    return ads_df


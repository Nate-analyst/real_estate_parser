import math

def data_filter(all_ads, parameters):

    filtered_ads = []

    for ad in all_ads:
        filtered_params = [param for param in ad["ad_parameters"] if param["pl"] in parameters]
        filtered_ads.append({
            'ad_id':ad['ad_id'],
            'ad_link':ad['ad_link'],
            'price_byn':math.ceil(int(ad['price_byn'])/100),
            'price_usd':math.ceil(int(ad['price_usd'])/100),
            'company_ad':ad['company_ad'],
            "filtered_parameters": filtered_params
        })

    return filtered_ads
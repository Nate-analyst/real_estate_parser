import requests
import math

def page_counter():
    count_url = f"https://api.kufar.by/search-api/v2/search/count?cat=1010&cur=USD&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MiwicGl0IjoiMjg5Mzg5OTAifQ%3D%3D&gtsy=country-belarus&size=200&typ=sell"
    response = requests.get(count_url)
    data = response.json()
    total_ads = data['count']

    ADS_PER_PAGE = 200

    amount_of_pages = math.ceil(total_ads / ADS_PER_PAGE)
    return amount_of_pages
import requests

def raw_data_parser(amount_of_pages):

    all_ads = []
    cursor = 'eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MX0='
    for page_number in range(1, amount_of_pages+1):
            
        try:

            url = f"https://api.kufar.by/search-api/v2/search/rendered-paginated?cat=1010&cur=USD&cursor={cursor}&gtsy=country-belarus&lang=ru&typ=sell&size=200"
                
            response = requests.get(url)
            data = response.json()
            
            for i in range(len(data['pagination']['pages'])):
                next_page = data['pagination']['pages'][i]['label']
                if next_page == "next":
                    cursor = data['pagination']['pages'][i]['token']

            ads = data.get("ads", [])
            all_ads.extend(ads)
            print(f"Page: {page_number} total_ads: {len(ads)}")

        except requests.exceptions.RequestException as e:
            print(f"Ошибка на странице {page_number}: {e}")
            continue

    return all_ads
            
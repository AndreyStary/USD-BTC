import requests
from bs4 import BeautifulSoup


DOLLAR_BTC = 'https://www.google.com/search?sxsrf=ALeKk02xAdqFLSzY7N364HA6_nWYMCToXw%3A1608541981032&ei=HWfgX77FAc' \
                 'v2qwHzjaXgDw&q=%D0%BA%D1%83%D1%80%D1%81+usd%2Fbtc&oq=%D0%BA%D1%83%D1%80%D1%81+usd%2Fbtc&gs_lcp=CgZw' \
             'c3ktYWIQAzIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIICAAQFhAKEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIICA' \
             'AQFhAKEB46BAgAEEc6AggAOgUIABCxAzoECAAQCjoHCAAQsQMQCjoPCAAQsQMQFBCHAhBGEIICOgcIABAUEIcCUNGuXli6zl5gudBea' \
             'AFwA3gAgAFbiAG1BJIBATiYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=psy-ab&ved=0ahUKEwj-x4rr3d7tAhVL-yoKHfNGCf' \
             'wQ4dUDCA0&uact=5'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/87.0.4280.88 Safari/537.36'}

print('Введите кол-во USD:')
USD = float(input())
print('Введите кол-во BTC:')
BTC = float(input())

print(f'Вы за {USD} долларов приобрели {BTC} биткоинов')

current_converted_price = 0

full_page = requests.get(DOLLAR_BTC, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')

convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 6})

currency = convert[0].text.replace(',', '.')
currency = float(currency)
new_btc = currency*USD

print(f'На данный момент за {USD} долларов вы можете приобрести {new_btc} BTC')

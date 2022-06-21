import requests
import json


try:
    url = "https://seller.wildberries.ru/ns/api/suppliers-portal-feedbacks-questions/api/v1/feedbacks"

    cookies = {
        "WBToken": "AvSQ7xPc9NaqDNywwKsMQgXJX2ivdxq6Fdv8RfBLDI2MvGiAI2CXG1Ts87FJ3K_"
                   "cOLhmxNja9IHkLuqipzixP1WrmvfRZS32AwD9eScVpMVlOw",
        "x-supplier-id": "15a693d3-6893-5f37-a4d0-8b850e623b57",
    }
    headers = {
        "content-type": "application/json",
        'Accept': '*/*',
        'Accept-Language': 'ru',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    body = {
        "id": "",
        "text": "",
        "state": "wbRu"
    }

    # r = requests.patch(url, data=json.dumps(body), cookies=cookies, headers=headers)
    r = requests.patch(url, json=body, cookies=cookies, headers=headers)
    # r = requests.patch(url, data=body, cookies=cookies, headers=headers)
    print(r, r.status_code)
except:
    print('Сайт недоступен')
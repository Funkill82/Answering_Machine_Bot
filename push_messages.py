# import requests


def push_answer_msg(dict_feedback):
    print("Сообщения отправлены")
    print(dict_feedback)

# try:
    # url = "https://seller.wildberries.ru/ns/api/suppliers-portal-feedbacks-questions/api/v1/feedbacks"

    # cookies = {
    #     'WBToken': 'AvSQ7xPc9NaqDNywwKsMQgXJX2ivdxq6Fdv8RfBLDI2MvGiAI2CXG1Ts87FJ3K_cOLhmxNja9IHkLuqipzixP1WrmvfRZS32AwD9eScVpMVlOw',
    #     'x-supplier-id': '15a693d3-6893-5f37-a4d0-8b850e623b57',
    # }
    # headers = {
    #     'Accept': '*/*',
    #     'Accept-Language': 'ru',
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36'
    #                   ' (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    # payload = {"id": "str-id", "text": str-text, "state": "wbRu"}

    # r = requests.patch(url,payload = , cookies=cookies, headers=headers)
    # print(r)
# except:
#     print('Сайт недоступен ')
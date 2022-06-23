import requests


def push_answer_msg(dict_feedback: dict):
    # def push_answer_msg(dict_feedback: dict, cookies_user: dict):

    try:
        url = "https://seller.wildberries.ru/ns/api/suppliers-portal-feedbacks-questions/api/v1/feedbacks"
        # cookies = cookies_user

        cookies = {
            "WBToken": "",
            "x-supplier-id": "",

        }
        headers = {

            'Accept': '*/*',
            'Accept-Language': 'ru',
            "content-type": "application/json",
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        body = dict_feedback

        r = requests.patch(url, json=body, cookies=cookies, headers=headers)
        if r.status_code >= 400:
            print('Ошибка запроса')
        else:
            print(r, r.status_code)
            print(dict_feedback)

    except:
        print('Сайт недоступен')

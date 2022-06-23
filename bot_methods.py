import requests
from notifier.app.auto_responder.push_messages import push_answer_msg
import random
import pandas


def get_excel(file: str) -> dict:
# def get_excel(file: str, username) -> dict:
    """ Обрабатывает файл шаблон, содержимое листов файла
        выгружается в словарь dict_xlsx"""
    try:
        try:
            dict_xlsx = {}
            excel_data = pandas.read_excel(file, sheet_name='Список обрабатываемых SKU')
            dict_xlsx["list_1_A"] = excel_data["SKU"][excel_data["SKU"].notnull()].tolist()
        except:
            # await send_message(username, "Файл шаблон содержит ошибку, лист - Список обрабатываемых SKU !")
            print("Файл шаблон содержит ошибку, лист - Список обрабатываемых SKU !")

        try:
            excel_data = pandas.read_excel(file, sheet_name='Ответы на отзывы')
            dict_xlsx["list_2_A"] = excel_data["Приветствие + спасибо за выбор"][
                excel_data["Приветствие + спасибо за выбор"].notnull()].tolist()
            dict_xlsx["list_2_B"] = excel_data["Благодарность"][excel_data["Благодарность"].notnull()].tolist()
            dict_xlsx["list_2_C"] = excel_data["Основной текст"][excel_data["Основной текст"].notnull()].tolist()
            dict_xlsx["list_2_D"] = excel_data["Прощание"][excel_data["Прощание"].notnull()].tolist()
        except:
            # await send_message(username, "Файл шаблон содержит ошибку, лист - Ответы на отзывы !")
            print("Файл шаблон содержит ошибку, лист - Ответы на отзывы !")

        try:
            excel_data = pandas.read_excel(file, sheet_name='Ответы на отзывы с id')
            dict_xlsx["list_3_A"] = excel_data["Приветствие + спасибо за выбор"][
                excel_data["Приветствие + спасибо за выбор"].notnull()].tolist()
            dict_xlsx["list_3_B"] = excel_data["Благодарность"][excel_data["Благодарность"].notnull()].tolist()
            dict_xlsx["list_3_C"] = excel_data["Основной текст"][excel_data["Основной текст"].notnull()].tolist()
            dict_xlsx["list_3_D"] = excel_data["Рекомендации"][excel_data["Рекомендации"].notnull()].tolist()
            dict_xlsx["list_3_E"] = excel_data["Прощание"][excel_data["Прощание"].notnull()].tolist()
        except:
            # await send_message(username, "Файл шаблон содержит ошибку, лист - Ответы на отзывы с id !")
            print("Файл шаблон содержит ошибку, лист - Ответы на отзывы с id !")

        try:
            excel_data = pandas.read_excel(file, sheet_name='Рекомендации')
            list_4_A = excel_data["Артикул"].tolist()
            list_4_B = excel_data["Название продукта"].tolist()
            list_4_C = excel_data["Артикул2"].tolist()
            list_4_D = excel_data["Для рекомендации"].tolist()

            # Словарь с рекомендациями
            # Собираю рекомендации с одинаковым СКУ в один список
            dict_xlsx["list_4"] = {}
            for i in range(len(list_4_A)):
                if list_4_A[i] in dict_xlsx["list_4"]:
                    dict_xlsx["list_4"][list_4_A[i]].append([list_4_B[i], list_4_D[i], list_4_C[i]])
                else:
                    dict_xlsx["list_4"].update({list_4_A[i]: [[list_4_B[i], list_4_D[i], list_4_C[i]]]})
        except:
            # await send_message(username, "Файл шаблон содержит ошибку, лист - Рекомендации !")
            print("Файл шаблон содержит ошибку, лист - Рекомендации !")

        excel_data = pandas.read_excel(file, sheet_name='Ключи подмены')
        list_5_A = excel_data["Ключ"].tolist()
        list_5_B = excel_data["Значение"].tolist()
        list_5_dict = {}
        # Вычисляю индексы расположения ключей
        index = [i for i in range(len(list_5_A)) if isinstance(list_5_A[i], str)]

        for i in range(len(index)):
            if i + 1 == len(index):
                list_5_dict[list_5_A[index[i]]] = list_5_B[index[i]:]
            else:
                list_5_dict[list_5_A[index[i]]] = list_5_B[index[i]:index[i + 1]]
        # Словарь с ключами подмены
        dict_xlsx["list_5"] = list_5_dict

        return dict_xlsx


    except:
        return False


def get_json(dict_xlsx: dict) -> bool:
    # def get_json(dict_xlsx: dict, cookies_user: dict) -> bool:
    """  По get запросу (с данными по селлеру-админу, его
        WBToken и x_supplier_id), достается json с отзывами
         на которые нет ответа"""
    try:
        step = 0
        cookies = {
            'WBToken': "AubT5hPa09aqDNqPwKsMQtohtRMELrrpHhLQI17wnuLO1TkRJdH6PppDtbcNgfTkGNncip77WzF1HDnbK5yf_e-A2XddN0_lTRxyvm80MUApBg",
            'x-supplier-id': "51de4438-9a42-5fdc-97a3-179e6e86a9b8",
        }
        # cookies = cookies_user
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru',
            "content-type": "application/json",
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        while True:
            # url = f"https://seller.wildberries.ru/ns/api/suppliers-portal-feedbacks-questions/api/v1/" \
            #       f"feedbacks?isAnswered=false&nmId=&order=dateDesc&skip={step}&take=1000"
            url = f"https://seller.wildberries.ru/ns/api/suppliers-portal-feedbacks-questions/api/v1/" \
                 f"feedbacks?isAnswered=false&metaDataKeyMustNot=norating&nmId=&order=dateDesc&skip={step}&take=1000"

            r = requests.get(url, cookies=cookies, headers=headers)
            json_data = r.json()
            data_list = get_data(json_data, dict_xlsx["list_1_A"])
            get_feedback_answer(data_list, dict_xlsx)
            # get_feedback_answer(data_list, dict_xlsx, cookies_user)
            if len(json_data['data'].get('feedbacks')) != 1000:
                return True
            step += 1000
    except:

        return False


def get_data(json_data: object, sku: list) -> list:
    """ Принимает json_data из него  достаю id,nmId 5-ти звездных
        отзывов, применяю  фильтр СКУ из списка sku, возвращаю
        data_list-список словарей"""
    data_list = []
    for item in json_data.get("data").get("feedbacks"):
        # Фильтр отзывов на 5 звезд и списка СКУ
        if item.get("productValuation") == 5 and item.get("nmId") in sku:
            data_list.append({"id": str(item.get("id")), "nmId": item.get("nmId")})

    return data_list


def get_feedback_answer(data_list: list, dict_xlsx: dict) -> dict:
    # def get_feedback_answer(data_list: list, dict_xlsx: dict, cookies_user):
    def key_replace(dict_x: dict, text: str) -> str:
        """На вход получает словарь и строку,
         ищет в строке ключи подмены, если находит
         достает из словаря значение соответсвующее
         данному ключу и подставляет его"""
        for key in dict_x['list_5'].keys():
            if text.find(key) != -1:
                key_value = random.choice(dict_x["list_5"].get(key))
                text = text.replace(key, key_value)

        return text

    for i in range(len(data_list)):
        nmId = data_list[i].get("nmId")
        dict_feedback = {}

        if nmId in dict_xlsx["list_4"]:
            # Достаю рамдомную рекомендацию по СКУ
            temp_list = random.choice(dict_xlsx["list_4"].get(nmId))

            random_text = f"{random.choice(dict_xlsx['list_3_A'])} {temp_list[0]} " \
                          f"{random.choice(dict_xlsx['list_3_B'])} {random.choice(dict_xlsx['list_3_C'])} " \
                          f"{random.choice(dict_xlsx['list_3_D'])} {temp_list[1]} Артикул:" \
                          f" {temp_list[2]}. {random.choice(dict_xlsx['list_3_E'])}"
            # Вызываю функцию подмены ключей
            random_text = key_replace(dict_xlsx, random_text)

        else:
            random_text = f"{random.choice(dict_xlsx['list_2_A'])}{random.choice(dict_xlsx['list_2_B'])}" \
                          f"{random.choice(dict_xlsx['list_2_C'])}{random.choice(dict_xlsx['list_2_D'])}"

            random_text = key_replace(dict_xlsx, random_text)
        # Отправляю сформированный словарь ответа
        dict_feedback = {"id": data_list[i].get("id"), "answer": {"text": random_text}, "state": "wbRu"}
        print(nmId)
        push_answer_msg(dict_feedback)
        # push_answer_msg(dict_feedback, cookies_user)

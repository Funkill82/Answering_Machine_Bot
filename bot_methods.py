# import requests
from push_messages import push_answer_msg
import random
import pandas


def get_excel(file) -> dict:
    """ Обрабатывае файл шаблон.xlsx, содержимое листов файла
        выгружается в словарь dict_xlsx"""
    try:

        dict_xlsx = {}
        excel_data = pandas.read_excel(file, sheet_name='Список обрабатываемых SKU')
        dict_xlsx["list_1_A"] = excel_data["SKU"][excel_data["SKU"].notnull()].tolist()

        excel_data = pandas.read_excel(file, sheet_name='Ответы на отзывы')
        dict_xlsx["list_2_A"] = excel_data["Приветствие + спасибо за выбор"][
            excel_data["Приветствие + спасибо за выбор"].notnull()].tolist()
        dict_xlsx["list_2_B"] = excel_data["Благодарность"][excel_data["Благодарность"].notnull()].tolist()
        dict_xlsx["list_2_C"] = excel_data["Основной текст"][excel_data["Основной текст"].notnull()].tolist()
        dict_xlsx["list_2_D"] = excel_data["Прощание"][excel_data["Прощание"].notnull()].tolist()

        excel_data = pandas.read_excel(file, sheet_name='Ответы на отзывы с id')
        dict_xlsx["list_3_A"] = excel_data["Приветствие + спасибо за выбор"][
            excel_data["Приветствие + спасибо за выбор"].notnull()].tolist()
        dict_xlsx["list_3_B"] = excel_data["Благодарность"][excel_data["Благодарность"].notnull()].tolist()
        dict_xlsx["list_3_C"] = excel_data["Основной текст"][excel_data["Основной текст"].notnull()].tolist()
        dict_xlsx["list_3_D"] = excel_data["Рекомендации"][excel_data["Рекомендации"].notnull()].tolist()
        dict_xlsx["list_3_E"] = excel_data["Прощание"][excel_data["Прощание"].notnull()].tolist()

        excel_data = pandas.read_excel(file, sheet_name='Рекомендации')
        list_4_A = excel_data["Артикул"].tolist()
        list_4_B = excel_data["Название продукта"].tolist()
        list_4_C = excel_data["Артикул2"].tolist()
        list_4_D = excel_data["Для рекомендации"].tolist()

        # Словарь с рекомендациями
        dict_xlsx["list_4"] = dict(zip(list_4_A, zip(list_4_B, list_4_D, list_4_C)))

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
    """ По get запросу (с данными по селлеру WBToken и
        x_supplier_id, достается json с отзывами на
        которые нет ответа"""
    try:
        step = 0
        # WBToken = None
        # x_supplier_id = None

        while True:
            url = f"https://seller.wildberries.ru/ns/api/suppliers-portal-feedbacks-questions/api/v1/" \
                  f"feedbacks?isAnswered=false&nmId=&order=dateDesc&skip={step}&take=1000"
            # cookies = {
            #     'WBToken': WBToken,
            #     'x-supplier-id': x_supplier_id,
            # }
            cookies = {

                'WBToken': 'AvSQ7xPc9NaqDNywwKsMQgXJX2ivdxq6Fdv8RfBLDI2MvGiAI2CXG1Ts87FJ3K_cOLhmxNja9IHkLuqipzixP1WrmvfRZS32AwD9eScVpMVlOw',
                'x-supplier-id': '15a693d3-6893-5f37-a4d0-8b850e623b57',
            }
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'ru',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36'
                              ' (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

            # r = requests.get(url, cookies=cookies, headers=headers)
            # json_data = r.json()
            json_data = {"data": {
                "countUnanswered": 133,
                "countArchive": 6739,
                "feedbacks": [
                    {
                        "id": "cNdvXIEBEUCUNtmVAFyM",
                        "imtId": 66479238,
                        "nmId": 83922684,
                        "subjectId": 2532,
                        "text": "Ecoco не подвели в очередной раз! Качество хорошее!",
                        "productValuation": 5,
                        "createdDate": "2022-06-13T09:39:46Z",
                        "updatedDate": None,
                        "answer": None,
                        "state": "none",
                        "productDetails": {
                            "imtId": 66479238,
                            "nmId": 83922684,
                            "productName": "Полка для ванной",
                            "supplierArticle": "ECO156/сер",
                            "supplierId": 54398,
                            "supplierName": "Индивидуальный предприниматель Суббота Руслан Сергеевич",
                            "brandId": 69583,
                            "brandName": "ECOCO"
                        },
                        "photos": [
                            {
                                "fullSizeUri": "feedbacks/6647/66479238/25974b0d-3dcb-48af-a6c7-9ffa1822849c_fs.jpg",
                                "minSizeUri": "feedbacks/6647/66479238/25974b0d-3dcb-48af-a6c7-9ffa1822849c_ms.jpg"
                            }
                        ],
                        "video": None,
                        "wasViewed": False
                    },
                    {
                        "id": "Pmw0XIEBkjR8f6ggSQRm",
                        "imtId": 11454882,
                        "nmId": 15331652,
                        "subjectId": 2532,
                        "text": "Отличная полка. Висит больше месяца. Понаставила и повесила на крючки кучу всякой всячины. Все держится.",
                        "productValuation": 5,
                        "createdDate": "2022-06-13T08:35:39Z",
                        "updatedDate": None,
                        "answer": None,
                        "state": "none",
                        "productDetails": {
                            "imtId": 11454882,
                            "nmId": 15331652,
                            "productName": "Полка для ванной",
                            "supplierArticle": "ЕСО076/011",
                            "supplierId": 54398,
                            "supplierName": "Индивидуальный предприниматель Суббота Руслан Сергеевич",
                            "brandId": 69583,
                            "brandName": "ECOCO"
                        },
                        "photos": None,
                        "video": None,
                        "wasViewed": False
                    },
                    {
                        "id": "hGEoVoEBjeZkdKc5ryeQ",
                        "imtId": 11454882,
                        "nmId": 15331652,
                        "subjectId": 2532,
                        "text": "Пришел целым, пластик гладкий, не воняет. Рекомендую.",
                        "productValuation": 5,
                        "createdDate": "2022-06-12T04:25:15Z",
                        "updatedDate": None,
                        "answer": None,
                        "state": "none",
                        "productDetails": {
                            "imtId": 11454882,
                            "nmId": 15331652,
                            "productName": "Полка для ванной",
                            "supplierArticle": "ЕСО076/011",
                            "supplierId": 54398,
                            "supplierName": "Индивидуальный предприниматель Суббота Руслан Сергеевич",
                            "brandId": 69583,
                            "brandName": "ECOCO"
                        },
                        "photos": None,
                        "video": None,
                        "wasViewed": False
                    }

                ]}}
            data_list = get_data(json_data, dict_xlsx["list_1_A"])
            get_feedback_answer(data_list, dict_xlsx)

            if len(json_data['data'].get('feedbacks')) != 1000:
                break
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


def get_feedback_answer(data_list: list, dict_xlsx: dict):


    def key_replace(dict_x: dict, text: str) -> str:
        """На вход получает словарь и строку,
         ищет в строке ключи подмены, если находит
         достает из словаря значение соответсвующее
         данному ключу и подставляет его"""
        for key in dict_x['list_5'].keys():
            if text.find(key) != -1:
                key_value = random.choice(dict_x["list_5"].get(key))
                text = random_text.replace(key, key_value)
                break
        return text

    for i in range(len(data_list)):
        nmId = data_list[i].get("nmId")
        dict_feedback = {}

        if nmId in dict_xlsx["list_4"]:

            random_text = f"{random.choice(dict_xlsx['list_3_A'])}{dict_xlsx['list_4'].get(nmId)[0]}" \
                          f"{random.choice(dict_xlsx['list_3_B'])}{random.choice(dict_xlsx['list_3_C'])}" \
                          f"{random.choice(dict_xlsx['list_3_D'])} {dict_xlsx['list_4'].get(nmId)[1]} Артикул:" \
                          f" {dict_xlsx['list_4'].get(nmId)[2]}. {random.choice(dict_xlsx['list_3_E'])}"

            random_text = key_replace(dict_xlsx, random_text)

        else:
            random_text = f"{random.choice(dict_xlsx['list_2_A'])}{random.choice(dict_xlsx['list_2_B'])}" \
                          f"{random.choice(dict_xlsx['list_2_C'])}{random.choice(dict_xlsx['list_2_D'])}"
            random_text = key_replace(dict_xlsx, random_text)
        # Отправляю сформированный словарь ответа
        dict_feedback = {"id": data_list[i].get("id"), "text": random_text, "state": "wbRu"}
        push_answer_msg(dict_feedback)


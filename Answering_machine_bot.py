import requests
import xlsxwriter
import json
import pandas
import random

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
            "id":"hGEoVoEBjeZkdKc5ryeQ",
            "imtId":11454882,
            "nmId":15331652,
            "subjectId":2532,
            "text":"Пришел целым, пластик гладкий, не воняет. Рекомендую.",
            "productValuation":5,
            "createdDate":"2022-06-12T04:25:15Z",
            "updatedDate":None,
            "answer":None,
            "state":"none",
            "productDetails":{
            "imtId":11454882,
            "nmId":15331652,
            "productName":"Полка для ванной",
            "supplierArticle":"ЕСО076/011",
            "supplierId":54398,
            "supplierName":"Индивидуальный предприниматель Суббота Руслан Сергеевич",
            "brandId":69583,
            "brandName":"ECOCO"
        },
        "photos":None,
        "video":None,
        "wasViewed":False
        }

    ]}}


def get_json(json_data, list_1_A):
    """ Принимаю json  достаю id отзывов """
    data_list = []

    for item in json_data.get("data").get("feedbacks"):
        # Фильтр отзывов на 5 звезд и списка СКУ
        if item.get("productValuation") == 5 and item.get("nmId") in list_1_A:
            data_list.append({"id": str(item.get("id")), "nmId": item.get("nmId")})
    return data_list


def get_excel():
    try:
        excel_data = pandas.read_excel('шаблон.xlsx', sheet_name='Список обрабатываемых SKU')
        list_1_A = excel_data["SKU"][excel_data["SKU"].notnull()].tolist()

        excel_data = pandas.read_excel('шаблон.xlsx', sheet_name='Ответы на отзывы')
        list_2_A = excel_data["Приветствие + спасибо за выбор"][
            excel_data["Приветствие + спасибо за выбор"].notnull()].tolist()
        list_2_B = excel_data["Благодарность"][excel_data["Благодарность"].notnull()].tolist()
        list_2_C = excel_data["Основной текст"][excel_data["Основной текст"].notnull()].tolist()
        list_2_D = excel_data["Прощание"][excel_data["Прощание"].notnull()].tolist()

        excel_data = pandas.read_excel('шаблон.xlsx', sheet_name='Ответы на отзывы с id')
        list_3_A = excel_data["Приветствие + спасибо за выбор"][
            excel_data["Приветствие + спасибо за выбор"].notnull()].tolist()
        list_3_B = excel_data["Благодарность"][excel_data["Благодарность"].notnull()].tolist()
        list_3_C = excel_data["Основной текст"][excel_data["Основной текст"].notnull()].tolist()
        list_3_D = excel_data["Рекомендации"][excel_data["Рекомендации"].notnull()].tolist()
        list_3_E = excel_data["Прощание"][excel_data["Прощание"].notnull()].tolist()

        excel_data = pandas.read_excel('шаблон.xlsx', sheet_name='Рекомендации')
        list_4_A = excel_data["Артикул"].tolist()
        list_4_B = excel_data["Название продукта"].tolist()
        list_4_C = excel_data["Артикул2"].tolist()
        list_4_D = excel_data["Для рекомендации"].tolist()

        # Словарь с рекомендациями
        list_4 = dict(zip(list_4_A, zip(list_4_B, list_4_D, list_4_C)))

        excel_data = pandas.read_excel('шаблон.xlsx', sheet_name='Ключи подмены')
        list_5_A = excel_data["Ключ"].tolist()
        list_5_B = excel_data["Значение"].tolist()

        list_5_dict = {}
        index = [i for i in range(len(list_5_A)) if isinstance(list_5_A[i], str)]

        for i in range(len(index)):
            if i + 1 == len(index):
                list_5_dict[list_5_A[index[i]]] = list_5_B[index[i]:]
            else:
                list_5_dict[list_5_A[index[i]]] = list_5_B[index[i]:index[i + 1]]

        return list_1_A, list_2_A, list_2_B, list_2_C, list_2_D, list_3_A, list_3_B, \
               list_3_C, list_3_D, list_3_E, list_4, list_5_dict


    except:
        print("Файл шаблон.xlsx отсутствует или возникли проблемы с его открытием!")


def get_feedback_5stars():
    list_1_A, list_2_A, list_2_B, list_2_C, list_2_D, list_3_A, list_3_B, \
    list_3_C, list_3_D, list_3_E, list_4, list_5_dict = get_excel()
    data_list = get_json(json_data, list_1_A)
    dict_feedback = {}

    for i in range(len(data_list)):
        nmId = data_list[i].get("nmId")

        if nmId in list_4:

            random_text = str(random.choice(list_3_A)) + list_4.get(nmId)[0] + str(random.choice(list_3_B)) + str(
                random.choice(list_3_C)) + str(random.choice(list_3_D)) + list_4.get(nmId)[1] + ' Артикул: ' + \
                          str(list_4.get(nmId)[2]) + ". " + str(random.choice(list_3_E))
        else:
            random_text = str(random.choice(list_2_A)) + str(random.choice(list_2_B)) + str(
                random.choice(list_2_C)) + str(random.choice(list_2_D))

        dict_feedback[i] = {"id": data_list[i].get("id"), "text": random_text, "state": "wbRu"}
    return dict_feedback


dict_feedback = get_feedback_5stars()
print(dict_feedback)

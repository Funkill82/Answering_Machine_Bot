# from aiogram import types
from notifier.app.auto_responder.bot_methods import get_excel, get_json
# from notifier.app.bot.bot_methods import send_message

def get_feedback_5stars(file_user: str):
# async def get_feedback_5stars(message):
    """Формирует рандомные сообщения на отзывы"""
    # username = msg.from_user.username
    # cookies_user = get_cookies(message)
    # file_user = download_file((message)
    dict_xlsx = get_excel(file_user)
    # dict_xlsx = get_excel(file_user, username)
    if not dict_xlsx:
        # await send_message(username, "Файл  отсутствует или возникли проблемы с его открытием!")
        print("Файл  отсутствует или возникли проблемы с его открытием!")
    else:
        # json_data = get_json(dict_xlsx, cookies_user)
        json_data = get_json(dict_xlsx)
        if not json_data:
            # await send_message(username, "Сайт недоступен")
            print('Сайт недоступен ')
        else:
            # await send_message(username, "Ответы на отзывы отправлены")
            print("Ответы на отзывы отправлены")


get_feedback_5stars("D:\All_projects\\notifier\\app\download_file\Ответы_на_отзывы_триммеры.xlsx")
#get_feedback_5stars(f"D:\\notifier\\app\download_file\{file_user}")

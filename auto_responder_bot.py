from aiogram import types
from bot_methods import get_excel, get_json
# from notifier.app.bot.bot_methods import send_message


def get_feedback_5stars(file):
    """Формирует рандомные сообщения на отзывы"""
    # username = msg.from_user.username
    dict_xlsx = get_excel(file)
    if not dict_xlsx:
        # await send_message(username, "Файл шаблон.xlsx отсутствует или возникли проблемы с его открытием!")
        print("Файл шаблон.xlsx отсутствует или возникли проблемы с его открытием!")
    else:
        json_data = get_json(dict_xlsx)
        if not json_data:
            # await send_message(username, "Сайт недоступен")
            print('Сайт недоступен ')

get_feedback_5stars('шаблон.xlsx')


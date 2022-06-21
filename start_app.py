from aiogram import types


async def bot_message(message: types.Message):
    await message.answer('Отправьте мне шаблон.xlsx')

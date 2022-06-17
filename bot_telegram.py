'''# МИНИМАЛЬНЫЙ КОД - echo БОТ
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_send(message : types.Message):
    await message.answer(message.text) #просто отвечает
    # await message.reply(message.text) #отвечает (комментируя твоё сообщение)
    # await bot.send_message(message.from_user.id, message.text) #отвечает в личку

executor.start_polling(dp, skip_updates=True)
'''
from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db

async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.sql_start()

from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

other.register_handlers_other(dp) #этот хендлер должен идти последним


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)











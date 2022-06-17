from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
    await message.reply('Здаров')

@dp.message_handler(commands=['комманда'])
async def echo(message: types.Message):
    await message.answer(message.text)

# @dp.message_handler(lambda message: 'такси' in message.text)
# async def taxi(message: types.Message):
#     await message.answer('Такси уже выехало')

@dp.message_handler(lambda message: 'нло' in message.text)
async def nlo(message: types.Message):
    await message.answer('Дурка уже выехало')

@dp.message_handler(lambda message: message.text.startswith('такси'))
async def price(message: types.Message):
    await message.answer(message.text[6:])

@dp.message_handler()
async def empty(message: types.Message):
    await message.answer('Нет такой команды')
    await message.delete()

executor.start_polling(dp, skip_updates=True)
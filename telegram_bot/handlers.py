from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from config import dp

@dp.message_handler(commands=['start'])   # команда  /start
async def on_start(message: Message):
    await message.answer(text=f' Приветствую тебя, {message.from_user.first_name}, твой id = {message.from_id}')


@dp.message_handler(Text('Привет!'))
async def on_start(message: Message):
    await message.answer(text=f' Привет!')

@dp.message_handler(Text('Пока!'))
async def on_start(message: Message):
    await message.answer(text=f' Пока!')
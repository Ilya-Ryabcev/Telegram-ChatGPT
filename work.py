import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

from aiogram.utils.keyboard import ReplyKeyboardBuilder

bot = Bot('7743295312:AAFmkYsQYr-5F_w4yaLBqZuI7btK6gmCaiY')
dp = Dispatcher()

@dp.message(Command('start'))
async def com_start(message:Message):
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='/start')
    keyboard.button(text='/random')
    keyboard.button(text='/jpt')

    await message.answer(
        text=f'Привет, {message.from_user.full_name}!\n Я готов к работе',
        reply_markup=keyboard.as_markup()
    )

@dp.message(Command('random'))
async def com_random(message:Message):
    await message.answer(
        text=f'Вы нажали кнопку random',
    )

@dp.message(Command('gpt'))
async def com_gpt(message:Message):
    await message.answer(
        text=f'Вы нажали кнопку jpt'
    )


async def start_bot():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start_bot())
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command

from aiogram.utils.keyboard import ReplyKeyboardBuilder

import os
import asyncio

bot = Bot(token=os.getenv('token'))
dp = Dispatcher()

@dp.message(Command('start'))
async def com_start(message:Message):
    await message.answer(
        text=f'Привет, {message.from_user.full_name}!\n Я готов к работе'
    )

@dp.message(Command('help'))
async def com_help(message: Message):
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(
        text='/help'
    )
    keyboard.button(
        text='/start'
    )

    await message.answer(
        text=f"Помоги себе сам!",
        reply_markup=keyboard.as_markup(),
    )

@dp.message(F.text.lower() == 'java')
async def com_help(message: Message):
    await message.answer(
        text=f"Привет java"
    )

@dp.message(F.text)
async def com_help(message: Message):
    await message.answer(
        text=f"Привет {message.text}"
    )

async def start_bot():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start_bot())

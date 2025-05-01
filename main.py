import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, BackgroundTypeWallpaper
from aiogram.filters import Command
import asyncio

from aiogram.utils.keyboard import ReplyKeyboardBuilder

bot = Bot(token=os.getenv('token'))
dp = Dispatcher()

@dp.message(Command('start'))
async def com_start(message:Message):
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='/start')
    keyboard.button(text='/random')
    keyboard.button(text='/jpt')
    keyboard.button(text='/talk')
    keyboard.button(text='/quiz')
    keyboard.button(text='/hobby')
    keyboard.button(text='/resman')

    await message.answer(
        text=f'Привет, {message.from_user.full_name}!\n Я готов к работе',
        reply_markup=keyboard.as_markup()
    )

@dp.message(Command('random'))
async def com_random(message:Message):
    await message.answer(
        text=f'Вы нажали кнопку random',
    )

@dp.message(Command('jpt'))
async def com_jpt(message:Message):
    await message.answer(
        text=f'Вы нажали кнопку jpt',
    )

@dp.message(Command('talk'))
async def com_talk(message:Message):
    await message.answer(
        text=f'Вы нажали кнопку talk',
    )

@dp.message(Command('quiz'))
async def com_quiz(message:Message):
    await message.answer(
        text=f'Вы нажали кнопку quiz'
    )

@dp.message(Command('hobby'))
async  def com_hobby(message:Message):
    await message.answer(
        text=f'Вы нажали кнопку hobby'
    )

@dp.message(Command('resman'))
async  def com_resman(message:Message):
    await message.answer(
        text=f'Вы нажали кнопку resman'
    )


async def start_bot():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start_bot())
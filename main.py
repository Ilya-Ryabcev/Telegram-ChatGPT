from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

bot = Bot(token='7743295312:AAFmkYsQYr-5F_w4yaLBqZuI7btK6gmCaiY')
dp = Dispatcher()

@dp.message(Command('start'))
async def com_start(message:Message):
    await message.answer(
        text=f'Привет, {message.from_user.full_name}!\n Я готов к работе'
    )








async def start_bot():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start_bot())
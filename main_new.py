from aiogram import Bot, Dispatcher
import asyncio
import os

bot = Bot(token=os.getenv('token'))
dp = Dispatcher()


async def start_bot():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start_bot())
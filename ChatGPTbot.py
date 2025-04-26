from aiogram import Bot, Dispatcher
import asyncio

bot = Bot(token='7743295312:AAFmkYsQYr-5F_w4yaLBqZuI7btK6gmCaiY')
dp = Dispatcher()


async def start_bot():
    dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start_bot())
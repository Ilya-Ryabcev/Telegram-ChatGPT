from aiogram import Bot, Dispatcher
import asyncio

bot = Bot(token='7743295312:AAFmkYsQYr-5F_w4yaLBqZuI7btK6gmCaiY')
dp = Dispatcher()

@dp.message
async def all_messages(message):
    print(message.from_user.full_name)

async def start_bot():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start_bot())

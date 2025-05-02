from aiogram import Bot, Dispatcher
import asyncio
import os
import misk
from handlers import main_router

bot = Bot(token=os.getenv('token'))
dp = Dispatcher()


async def start_bot():
    dp.startup.register(misk.on_start)
    dp.shutdown.register(misk.on_finish)
    dp.include_router(main_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        pass
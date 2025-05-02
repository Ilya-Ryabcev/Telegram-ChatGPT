from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
import os
from keyboards import kb_main_menu

command_router = Router()

@command_router.message(Command('start'))
async def com_start(message: Message):
    photo_path = os.path.join('resources', 'images', 'main.jpg')
    text_path = os.path.join('resources', 'messages', 'main.txt')
    photo = FSInputFile(photo_path)
    with open(text_path, 'r', encoding='UTF-8') as file:
        msg_text = file.read()
    await message.answer_photo(
        photo=photo,
        caption=msg_text,
        reply_markup=kb_main_menu(),
    )
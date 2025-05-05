from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("help"))
async def start_handler(message: Message):
    await message.answer("Qanday yordam kerak?")
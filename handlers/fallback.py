from aiogram import Router
from aiogram.types import Message

from static.constants import Messages


router = Router()


@router.message()
async def unknown_message(message: Message):
    await message.answer(Messages.UNKNOWN)
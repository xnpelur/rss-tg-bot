from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from static.constants import Buttons
from static.states import States
from handlers.commands import command_start_handler


router = Router()


@router.message(States.SOURCE_MANAGEMENT, F.text == Buttons.ADD_SOURCE)
async def add_source(message: Message):
    await message.answer("add source")


@router.message(States.SOURCE_MANAGEMENT, F.text == Buttons.REMOVE_SOURCE)
async def remove_source(message: Message):
    await message.answer("remove source")


@router.message(States.SOURCE_MANAGEMENT, F.text == Buttons.BACK_TO_MAIN)
async def back_to_main(message: Message, state: FSMContext):
    await command_start_handler(message, state)
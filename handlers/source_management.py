from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

from static.constants import Buttons, Messages, SOURCES
from static.states import States
from handlers.commands import command_start_handler


router = Router()


@router.message(States.SOURCE_MANAGEMENT, F.text == Buttons.ADD_SOURCE)
async def add_source(message: Message, state: FSMContext):
    await state.set_state(States.ADDING_SOURCE)
    await message.answer(Messages.ADDING_SOURCE, reply_markup=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=key) for key, _ in SOURCES.items()],
            [KeyboardButton(text=Buttons.BACK)]
        ], 
        resize_keyboard=True
    ))


@router.message(States.SOURCE_MANAGEMENT, F.text == Buttons.REMOVE_SOURCE)
async def remove_source(message: Message):
    await message.answer("remove source")


@router.message(States.SOURCE_MANAGEMENT, F.text == Buttons.BACK)
async def back_to_main(message: Message, state: FSMContext):
    await command_start_handler(message, state)
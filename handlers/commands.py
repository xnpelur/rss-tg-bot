from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.fsm.context import FSMContext

from static.constants import Messages, Buttons
from static.states import States


router = Router()


@router.message(Command("start"))
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(States.WELCOME)
    await message.answer(Messages.WELCOME, reply_markup=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=Buttons.GET_ARTICLE)], 
            [KeyboardButton(text=Buttons.MANAGE_SOURCES)]
        ], 
        resize_keyboard=True
    ))
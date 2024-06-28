import math
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

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
async def remove_source(message: Message, state: FSMContext):
    state_data = await state.get_data()

    if not "feeds" in state_data or len(state_data["feeds"]) == 0:
        await state.set_state(States.SOURCE_MANAGEMENT)
        await message.answer(Messages.URLS_EMPTY, reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=Buttons.ADD_SOURCE), KeyboardButton(text=Buttons.REMOVE_SOURCE)], 
                [KeyboardButton(text=Buttons.BACK)]
            ], 
            resize_keyboard=True
        ))
        return

    titles = [feed["title"] for feed in state_data["feeds"]]
    list_items = [f"{i + 1}. {title}" for i, title in enumerate(titles)]

    keyboard = [
        [
            KeyboardButton(text=str(row * 3 + i + 1) if row * 3 + i < len(list_items) else " ") 
            for i in range(3)
        ]
        for row in range(math.ceil(len(list_items) / 3))
    ]
    keyboard.append([KeyboardButton(text=Buttons.BACK)])

    await message.answer(
        Messages.REMOVING_SOURCE + "\n\n" + "\n".join(list_items),
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard,
        resize_keyboard=True)
    )
    await state.set_state(States.REMOVING_SOURCE)


@router.message(States.SOURCE_MANAGEMENT, F.text == Buttons.BACK)
async def back_to_main(message: Message, state: FSMContext):
    await command_start_handler(message, state)
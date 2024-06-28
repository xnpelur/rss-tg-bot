from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from static.constants import Buttons, Messages, SOURCES
from static.states import States
from handlers.welcome import manage_sources
from handlers.source_management import remove_source


router = Router()


@router.message(States.REMOVING_SOURCE, F.text == Buttons.BACK)
async def back(message: Message, state: FSMContext):
    await manage_sources(message, state)


@router.message(States.REMOVING_SOURCE)
async def removing_source(message: Message, state: FSMContext):
    try:
        index = int(message.text) - 1
        if index < 0:
            raise Exception()
        state_data = await state.get_data()

        removed = state_data["feeds"].pop(index)
        await state.set_data(state_data)

        await message.answer(f'{Messages.REMOVING_SOURCE_SUCCESS}: "{removed["title"]}"')
        await remove_source(message, state)
    except Exception as e:
        await message.answer(Messages.ERROR)
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from static.constants import Buttons, Messages, SOURCES
from static.states import States
from lib.rss import get_feed_title
from handlers.welcome import manage_sources


router = Router()


@router.message(States.ADDING_SOURCE, F.text == Buttons.BACK)
async def back(message: Message, state: FSMContext):
    await manage_sources(message, state)


@router.message(States.ADDING_SOURCE)
async def adding_source(message: Message, state: FSMContext):
    url = SOURCES.get(message.text, message.text)

    try:
        title = get_feed_title(url)
        await message.answer(f'{Messages.ADDING_SOURCE_SUCCESS}: "{title}"')
    except Exception as e:
        await message.answer(Messages.ERROR)
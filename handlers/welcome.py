from aiogram import Router, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.fsm.context import FSMContext

from lib.randomizer import get_random_article 
from static.constants import Messages, Buttons
from static.states import States


router = Router()


@router.message(States.WELCOME, F.text == Buttons.GET_ARTICLE)
async def send_random_article(message: Message):
    urls = ["https://habr.com/ru/rss/articles/?fl=ru"]
    article = get_random_article(urls)
    if not article:
        await message.answer(Messages.ERROR)
    else:
        text = "\n\n".join([
            f"<b>{article.title}</b>", 
            article.description, 
            f'<a href="{article.link}">Читать полностью</a>'
        ])
        if len(article.image_url) > 0:
            await message.answer_photo(article.image_url, text)
        else:
            await message.answer(text)


@router.message(States.WELCOME, F.text == Buttons.MANAGE_SOURCES)
async def manage_sources(message: Message, state: FSMContext):
    await state.set_state(States.SOURCE_MANAGEMENT)
    await message.answer(Messages.SOURCES_MANAGEMENT, reply_markup=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=Buttons.ADD_SOURCE)], 
            [KeyboardButton(text=Buttons.REMOVE_SOURCE)],
            [KeyboardButton(text=Buttons.BACK_TO_MAIN)]
        ], 
        resize_keyboard=True
    ))


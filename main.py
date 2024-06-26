import asyncio
import logging
import sys

from dotenv import load_dotenv
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

from randomizer import get_random_article 


load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

# Constants
WELCOME_TEXT = "Приветствую! Нажмите кнопку, чтобы получить случайную статью"
GET_ARTICLE_TEXT = "Получить статью"
UNKNOWN_MESSAGE_TEXT = "Сообщение не распознано"
ERROR_TEXT = "Что-то пошло не так, пожалуйста повторите попытку"


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    button = KeyboardButton(text=GET_ARTICLE_TEXT)
    markup = ReplyKeyboardMarkup(keyboard=[[button]], resize_keyboard=True)

    await message.answer(WELCOME_TEXT, reply_markup=markup)


@dp.message()
async def echo_handler(message: Message) -> None:
    if message.text == GET_ARTICLE_TEXT:
        await send_random_article(message)
    else:
        await message.answer(UNKNOWN_MESSAGE_TEXT)


async def send_random_article(message: Message):
    urls = ["https://habr.com/ru/rss/articles/?fl=ru"]
    article = get_random_article(urls)
    if not article:
        await message.answer(ERROR_TEXT)
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


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
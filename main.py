import asyncio
import logging
import sys

from dotenv import load_dotenv
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from randomizer import get_random_article 


load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    urls = ["https://habr.com/ru/rss/articles/?fl=ru"]
    article = get_random_article(urls)
    if not article:
        await message.answer("Что-то пошло не так, пожалуйста повторите попытку")
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


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
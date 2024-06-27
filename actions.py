from aiogram.types import Message

from randomizer import get_random_article 
from constants import Messages

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

async def add_source(message: Message):
    await message.answer("add source")

async def remove_source(message: Message):
    await message.answer("remove source")
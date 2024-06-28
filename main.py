import asyncio
import logging
import sys

from dotenv import load_dotenv
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.mongo import MongoStorage

from handlers import commands, welcome, source_management, adding_source, removing_source, fallback


load_dotenv()

TOKEN = getenv("BOT_TOKEN")
MONGO_HOST = getenv("MONGO_HOST")
MONGO_PORT = int(getenv("MONGO_PORT"))


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    storage = MongoStorage.from_url(f"mongodb://{MONGO_HOST}:{MONGO_PORT}")
    dp = Dispatcher(storage=storage)
    dp.include_routers(
        commands.router, 
        welcome.router, 
        source_management.router, 
        adding_source.router,
        removing_source.router,
        fallback.router
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
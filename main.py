import asyncio
import logging
import sys

from dotenv import load_dotenv
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.commands import router as commands_router
from handlers.welcome import router as welcome_router
from handlers.source_management import router as source_management_router
from handlers.fallback import router as fallback_router


load_dotenv()
TOKEN = getenv("BOT_TOKEN")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_routers(commands_router, welcome_router, source_management_router, fallback_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
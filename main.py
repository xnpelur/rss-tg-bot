import asyncio
import logging
import sys

import actions

from dotenv import load_dotenv
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

from constants import Messages, Buttons


load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(Messages.WELCOME, reply_markup=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=Buttons.GET_ARTICLE)], 
            [KeyboardButton(text=Buttons.MANAGE_SOURCES)]
        ], 
        resize_keyboard=True
    ))


@dp.message()
async def message_handler(message: Message) -> None:
    match message.text:
        case Buttons.GET_ARTICLE:
            await actions.send_random_article(message)
        case Buttons.ADD_SOURCE:
            await actions.add_source(message)
        case Buttons.REMOVE_SOURCE:
            await actions.remove_source(message)
        case Buttons.BACK_TO_MAIN:
            await command_start_handler(message)
        case Buttons.MANAGE_SOURCES:
            await message.answer(Messages.SOURCES_MANAGEMENT, reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text=Buttons.ADD_SOURCE)], 
                    [KeyboardButton(text=Buttons.REMOVE_SOURCE)],
                    [KeyboardButton(text=Buttons.BACK_TO_MAIN)]
                ], 
                resize_keyboard=True
            ))
        case _:
            await message.answer(Messages.UNKNOWN)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
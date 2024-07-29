import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from db_manager import db_manager
from routers.create import router as create_router
from routers.delete import router as delete_router
from routers.edit import router as edit_router
from tools import show_tasks

TOKEN = "7004254683:AAGPcRYXFVVz_zr2caoRqV7kdMMUnXbEQoc"
dp = Dispatcher()

dp.include_router(create_router)
dp.include_router(edit_router)
dp.include_router(delete_router)


@dp.message(Command("test"))
async def test(message: Message) -> None:
    await message.answer("Hello", reply_markup=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='text1'), KeyboardButton(text='text3')],
            [KeyboardButton(text='text2')]
        ]
    ), )


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.full_name}! {message.from_user.id}")


@dp.message(Command("show_all"))
async def show_all(message: Message):
    tasks = db_manager.get_all_tasks(message.from_user.id)
    await message.answer(show_tasks(tasks))


@dp.message(Command("edit_task"))
async def edit(message: Message):
    text = message.text
    title_description = text.split(" ", 1)[1]
    title, new_description = title_description.split(". ")

    db_manager.edit_task(title, new_description, message.from_user.id)
    await message.answer("Changed!")


# @dp.message()
# async def echo_handler(message: Message) -> None:
#     await message.answer(f"ви написали {message.text}")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

""""
/create
Бот: Введіть назву задачі
К: Прибирання
Бот: введіть опис
К: ...
Бот: Задачу створено!


"""

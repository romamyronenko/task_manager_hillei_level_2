from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from db_manager import db_manager
from tools import show_tasks


class Form(StatesGroup):
    delete_title = State()


router = Router()


@router.message(Command("delete"))
async def delete(message: Message, state: FSMContext):
    text = message.text
    if text == "/delete":
        tasks = db_manager.get_all_tasks(message.from_user.id)
        await message.answer(show_tasks(tasks))
        buttons = []
        for task in tasks:
            buttons.append(KeyboardButton(text=f'{task[1]}({task[0]})'))
        await message.answer(
            "Оберіть задачу яку ви хочете видалити:",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    buttons
                ]
            ),
        )
        await state.set_state(Form.delete_title)
    else:
        id_ = text.split(" ", 1)[1]

        db_manager.delete_task(id_, message.from_user.id)

        await message.answer("Task removed")


@router.message(Form.delete_title)
async def get_title(message: Message, state: FSMContext):
    text = message.text
    id_ = text.split("(", 1)[1][:-1]
    db_manager.delete_task(id_, message.from_user.id)
    await message.answer("Задачу видалено!", reply_markup=ReplyKeyboardRemove())
    await state.clear()

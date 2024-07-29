import re

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from db_manager import db_manager
from tools import show_tasks, create_tasks_keyboard


class Form(StatesGroup):
    delete_title = State()


router = Router()


@router.message(F.text.regexp(r"^/delete [0-9]+$"))
async def delete_one_line(message: Message, state: FSMContext):
    text = message.text

    id_ = text.split(" ", 1)[1]

    db_manager.delete_task(id_, message.from_user.id)

    await message.answer("Task removed")


@router.message(F.text.regexp(r"^/delete$"))
async def delete(message: Message, state: FSMContext):
    tasks = db_manager.get_all_tasks(message.from_user.id)
    await message.answer(show_tasks(tasks))

    await message.answer(
        "Оберіть задачу яку ви хочете видалити:",
        reply_markup=create_tasks_keyboard(tasks),
    )
    await state.set_state(Form.delete_title)


@router.message(Form.delete_title)
async def get_title(message: Message, state: FSMContext):
    text = message.text
    id_ = text.split("(", 1)[1][:-1]
    db_manager.delete_task(id_, message.from_user.id)
    await message.answer("Задачу видалено!", reply_markup=ReplyKeyboardRemove())
    await state.clear()

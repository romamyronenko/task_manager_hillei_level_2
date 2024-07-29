from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from db_manager import db_manager
from tools import show_tasks, create_tasks_keyboard


class Form(StatesGroup):
    edit_title = State()
    edit_description = State()


router = Router()


@router.message(F.text.regexp(r"^/edit [0-9]+ (.|\n)+$"))
async def edit_one_line(message: Message, state: FSMContext):
    text = message.text  # те,що написав користувач
    id_description = text.split(" ", 1)[1]
    id_, new_description = id_description.split(" ")

    db_manager.edit_task(id_, new_description, message.from_user.id)
    await message.answer("Changed!")


@router.message(F.text.regexp(r"^/edit"))
async def edit(message: Message, state: FSMContext):
    tasks = db_manager.get_all_tasks(message.from_user.id)
    await message.answer(show_tasks(tasks))

    await message.answer('Введіть назву задачі яку хочете змінити: ', reply_markup=create_tasks_keyboard(tasks))
    await state.set_state(Form.edit_title)


@router.message(Form.edit_title)
async def get_title(message: Message, state: FSMContext):
    text = message.text
    id_ = text.split("(", 1)[1][:-1]

    await state.update_data(id=id_)  # Цей ""state data зберігає наш title
    await state.set_state(Form.edit_description)
    await message.answer('Напишіть новий опис задачі:')


@router.message(Form.edit_description)
async def description(message: Message, state: FSMContext):
    new_description = message.text
    data = await state.get_data()
    id_ = data['id']
    db_manager.edit_task(id_, new_description, message.from_user.id)
    await message.answer(f'Задача "{id_}" змінена')
    await state.clear()

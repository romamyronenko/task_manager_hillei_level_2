from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from db_manager import db_manager


class Form(StatesGroup):
    edit_title = State()
    edit_description = State()


router = Router()


@router.message(Command("edit"))
async def create(message: Message, state: FSMContext):
    text = message.text
    if text == '/edit':
        await message.answer('Введіть назву задачі яку хочете змінити: ')
        await state.set_state(Form.edit_title)
    else:
        text = message.text  # те,що написав користувач
        title_description = text.split(" ", 1)[1]
        title, new_description = title_description.split(". ")

        db_manager.edit_task(title, new_description, message.from_user.id)
        await message.answer("Changed!")


@router.message(Form.edit_title)
async def title(message: Message, state: FSMContext):
    title = message.text
    await state.update_data(title=title)  # Цей ""state data зберігає наш title
    await state.set_state(Form.edit_description)
    await message.answer('Напишіть новий опис задачі:')


@router.message(Form.edit_description)
async def description(message: Message, state: FSMContext):
    new_description = message.text
    data = await state.get_data()
    title = data['title']
    db_manager.edit_task(title, new_description, message.from_user.id)
    await message.answer(f'Задача "{title}" змінена')
    await state.clear()

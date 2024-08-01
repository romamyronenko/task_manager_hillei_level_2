from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from db_manager import db_manager


class Form(StatesGroup):
    title = State()
    description = State()


router = Router()


@router.message(F.text.regexp(r"^/create$"))
async def create(message: Message, state: FSMContext):
    await message.answer('Введіть назву задачі: ')
    await state.set_state(Form.title)


@router.message(F.text.regexp(r"^/create \w+\.\s\w+$"))
async def delete_one_line(message: Message, state: FSMContext):
    text = message.text
    title_description = text.split(" ", 1)[1]
    title, description = title_description.split(". ", 1)
    task = {'title': title, "description": description, "user_id": message.from_user.id}
    db_manager.add_task(task)
    await message.answer(f'title: {title}\ndescription: {description}')


@router.message(Form.title)
async def get_title(message: Message, state: FSMContext):
    title = message.text
    await state.update_data(title=title)  # Цей ""state data зберігає наш title
    await state.set_state(Form.description)
    await message.answer('Напишіть опис задачі:')


@router.message(Form.description)
async def get_description(message: Message, state: FSMContext):
    description = message.text
    data = await state.get_data()
    title = data['title']
    task = {'title': title, "description": description, "user_id": message.from_user.id}
    db_manager.add_task(task)
    await message.answer(f'title: {title}\ndescription: {description}')
    await state.clear()

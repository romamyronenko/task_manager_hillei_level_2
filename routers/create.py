from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from db_manager import db_manager


class Form(StatesGroup):
    title = State()
    description = State()


router = Router()


@router.message(Command("create"))
async def create(message: Message, state: FSMContext):
    text = message.text
    if text == '/create':
        await message.answer('Введіть назву задачі: ')
        await state.set_state(Form.title)
    else:
        title_description = text.split(" ", 1)[1]
        title, description = title_description.split(". ", 1)
        task = {'title': title, "description": description, "user_id": message.from_user.id}
        db_manager.add_task(task)
        await message.answer(f'title: {title}\ndescription: {description}')


@router.message(Form.title)
async def get_title(message: Message, state: FSMContext):
    title = message.text
    await state.update_data(title=title)
    await state.set_state(Form.description)
    await message.answer('Напишіть опис задачі!')


@router.message(Form.description)
async def get_description(message: Message, state: FSMContext):
    description = message.text
    data = await state.get_data()
    title = data['title']
    task = {'title': title, "description": description, "user_id": message.from_user.id}
    db_manager.add_task(task)
    await message.answer(f'title: {title}\ndescription: {description}')
    await state.clear()


"""
/create asd. ascxsad

state: Form.description
state.data: {'title': "EDFweaF"}

description: "ASD32W DQ3EWFQ234FQ423TFQ234F"
title: "EDFweaF"
"""
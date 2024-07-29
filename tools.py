from aiogram import html
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def show_tasks(tasks):
    lines = []

    for task in tasks:
        lines.append(f"{html.bold(task[1])}\nid: {task[0]}\n{task[2]}")
    return "\n\n".join(lines)


def create_tasks_keyboard(tasks):
    buttons = []
    for task in tasks:
        buttons.append(KeyboardButton(text=f'{task[1]}({task[0]})'))

    return ReplyKeyboardMarkup(
        keyboard=[
            buttons
        ]
    )

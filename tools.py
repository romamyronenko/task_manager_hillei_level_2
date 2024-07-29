from aiogram import html


def show_tasks(tasks):
    lines = []

    for task in tasks:
        lines.append(f"{html.bold(task[1])}\nid: {task[0]}\n{task[2]}")
    return "\n\n".join(lines)

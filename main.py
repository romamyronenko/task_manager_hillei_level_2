tasks = []


def create_task():
    title = input('введіть назву: ')
    description = input('введіть опис: ')
    task = {'title': title, "description": description}
    tasks.append(task)


def show_all_tasks():
    print(tasks)


def change_task():
    title = input("введіть назву задачі яку ви хочете видалити: ")
    for task in tasks:
        if task['title'] == title:
            print(f"Задача: {task}")
            description = input('введіть новий опис')
            task['description'] = description


def delete_task():
    title = input("введіть назву задачі яку ви хочете видалити: ")
    for task in tasks:
        if task['title'] == title:
            tasks.remove(task)


def get_commands_list(cmds):
    lines = []
    for key, value in cmds.items():
        lines.append(f'{key}. {value['description']}')

    return "\n".join(lines)


commands = {
    '1': {'func': create_task, "description": "Створити задачу"},
    '2': {'func': show_all_tasks, "description": "Переглянути всі задачі"},
    '3': {'func': change_task, "description": "Змінити задачу"},
    '4': {'func': delete_task, "description": "Видалити задачу"},
}

commands_descriptions = get_commands_list(commands)
menu = f"Оберіть дію: \n{commands_descriptions}"

while True:
    cmd = input(menu)
    if not cmd:
        break

    if cmd in commands:
        commands[cmd]['func']()
    else:
        print('Невірна команда!')

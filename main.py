from dispatcher import Dispatcher
from file_manager import TextFileManager
from filters import Command, CommandWithParams

file_manager = TextFileManager("data.txt")
# file_manager = JSONFileManager("data.json")


dispatcher = Dispatcher()

"""
handlers = [
    {'func': create_task, 'filter': Command('create'), 'description': "Створити задачу"},
    {'func': create_task_, 'filter': CommandWithParam('create'), 'description': "Створити задачу"},
    {'func': show_all_tasks, 'filter': Command('show_all'), 'description': "Переглянути всі задачі"},
    
]

message: "/create asd  asd asd "

cmd = Command('show_all')
cmd.check("/show_all")
"""


@dispatcher.handle_message(Command('create'), "Створити задачу")
def create_task(message: str):
    title = input('введіть назву: ')
    description = input('введіть опис: ')
    task = {'title': title, "description": description}

    tasks = file_manager.read_from_file()
    tasks.append(task)
    file_manager.write_to_file(tasks)


@dispatcher.handle_message(CommandWithParams('create'), "Створити задачу з вказаними параметрами")
def create_task_(message: str):
    """
    message: "/create Прибирання в кімнаті. Помити підлогу, протерти пил"
    ["/create", "Прибирання в кімнаті. Помити підлогу, протерти пил"]

    """
    title_description = message.split(' ', 1)[1]
    title, description = title_description.split('. ', 1)

    task = {'title': title, "description": description}

    tasks = file_manager.read_from_file()
    tasks.append(task)
    file_manager.write_to_file(tasks)


@dispatcher.handle_message(Command('show_all'), "Переглянути всі задачі")
def show_all_tasks(message: str):
    print(file_manager.read_from_file())


@dispatcher.handle_message(Command('edit'), "Змінити задачу")
def change_task(message: str):
    tasks = file_manager.read_from_file()
    title = input("введіть назву задачі яку ви хочете видалити: ")
    for task in tasks:
        if task['title'] == title:
            print(f"Задача: {task}")
            description = input('введіть новий опис')
            task['description'] = description
    file_manager.write_to_file(tasks)


@dispatcher.handle_message(Command('delete'), "Видалити задачу")
def delete_task(message: str):
    title = input("введіть назву задачі яку ви хочете видалити: ")

    tasks = file_manager.read_from_file()
    for task in tasks:
        if task['title'] == title:
            tasks.remove(task)
    file_manager.write_to_file(tasks)


dispatcher.run()

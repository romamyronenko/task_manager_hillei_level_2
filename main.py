from dispatcher import Dispatcher
from file_manager import DBManager
from filters import Command, CommandWithParams

file_manager = DBManager("database")

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

    file_manager.add_task(task)


@dispatcher.handle_message(CommandWithParams('create'), "Створити задачу з вказаними параметрами")
def create_task_(message: str):
    """
    message: "/create Прибирання в кімнаті. Помити підлогу, протерти пил"
    ["/create", "Прибирання в кімнаті. Помити підлогу, протерти пил"]

    """
    title_description = message.split(' ', 1)[1]
    title, description = title_description.split('. ', 1)

    task = {'title': title, "description": description}

    file_manager.add_task(task)


@dispatcher.handle_message(Command('show_all'), "Переглянути всі задачі")
def show_all_tasks(message: str):
    print(file_manager.get_all_tasks())


@dispatcher.handle_message(Command('edit'), "Змінити задачу")
def change_task(message: str):
    title = input("введіть назву задачі яку ви хочете змінити: ")

    description = input('введіть новий опис')
    file_manager.edit_task(title, description)


@dispatcher.handle_message(Command('delete'), "Видалити задачу")
def delete_task(message: str):
    title = input("введіть назву задачі яку ви хочете видалити: ")

    file_manager.delete_task(title)


@dispatcher.handle_message(CommandWithParams('edit'), 'Змінити задачу ')
def change(message: str):
    title_description = message.split(' ', 1)[1]
    title, new_description = title_description.split('. ', 1)

    file_manager.edit_task(title, new_description)


@dispatcher.handle_message(CommandWithParams('delete'), "Видалити задачу")
def delete_task(message: str):
    title = message.split(' ', 1)[1]

    file_manager.delete_task(title)


dispatcher.run()

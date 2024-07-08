from dispatcher import Dispatcher
from file_manager import TextFileManager

file_manager = TextFileManager("data.txt")
# file_manager = JSONFileManager("data.json")


dispatcher = Dispatcher()


@dispatcher.handle_message('1', "Створити задачу")
def create_task():
    title = input('введіть назву: ')
    description = input('введіть опис: ')
    task = {'title': title, "description": description}

    tasks = file_manager.read_from_file()
    tasks.append(task)
    file_manager.write_to_file(tasks)


@dispatcher.handle_message('2', "Переглянути всі задачі")
def show_all_tasks():
    print(file_manager.read_from_file())


@dispatcher.handle_message('3', "Змінити задачу")
def change_task():
    tasks = file_manager.read_from_file()
    title = input("введіть назву задачі яку ви хочете видалити: ")
    for task in tasks:
        if task['title'] == title:
            print(f"Задача: {task}")
            description = input('введіть новий опис')
            task['description'] = description
    file_manager.write_to_file(tasks)


@dispatcher.handle_message("4", "Видалити задачу")
def delete_task():
    title = input("введіть назву задачі яку ви хочете видалити: ")

    tasks = file_manager.read_from_file()
    for task in tasks:
        if task['title'] == title:
            tasks.remove(task)
    file_manager.write_to_file(tasks)


dispatcher.run()

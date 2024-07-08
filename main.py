from dispatcher import Dispatcher
from file_manager import write_to_file, read_from_file

filename = "data.txt"

dispatcher = Dispatcher()


@dispatcher.handle_message('1', "Створити задачу")
def create_task():
    title = input('введіть назву: ')
    description = input('введіть опис: ')
    task = {'title': title, "description": description}

    tasks = read_from_file(filename)
    tasks.append(task)
    write_to_file(tasks, filename)


@dispatcher.handle_message('2', "Переглянути всі задачі")
def show_all_tasks():
    print(read_from_file(filename))


@dispatcher.handle_message('3', "Змінити задачу")
def change_task():
    tasks = read_from_file(filename)
    title = input("введіть назву задачі яку ви хочете видалити: ")
    for task in tasks:
        if task['title'] == title:
            print(f"Задача: {task}")
            description = input('введіть новий опис')
            task['description'] = description
    write_to_file(tasks, filename)


@dispatcher.handle_message("4", "Видалити задачу")
def delete_task():
    title = input("введіть назву задачі яку ви хочете видалити: ")

    tasks = read_from_file(filename)
    for task in tasks:
        if task['title'] == title:
            tasks.remove(task)
    write_to_file(tasks, filename)


dispatcher.run()

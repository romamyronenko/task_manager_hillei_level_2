tasks = [
    {"title": "asd", "description": "dsa"},
    {"title": "Прибирання", "description": "ПРибьрати у кімнаті"},
]


def format_task(task):
    return f'{task["title"]} | {task["description"]}'


def write_to_file(task_list: list[dict], filename: str):
    to_write = [format_task(task) for task in task_list]

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(to_write))


def parse_str(s):
    title, description = s.strip().split(' | ')
    return {
        'title': title,
        'description': description
    }


def read_from_file(filename):
    task_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            task_list.append(parse_str(line))

    return task_list


"""
line: asd | dsa

"""

# save_to_file(tasks, "data.txt")
tasks = read_from_file("data.txt")
print(tasks)

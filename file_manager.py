def write_to_file(task_list: list[dict], filename: str) -> None:
    to_write = [_format_task(task) for task in task_list]

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(to_write))


def read_from_file(filename: str) -> list[dict]:
    task_list = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                task_list.append(_parse_str(line))
    except:
        pass
    return task_list


def _format_task(task: dict) -> str:
    return f'{task["title"]} | {task["description"]}'


def _parse_str(s: str) -> dict:
    title, description = s.strip().split(' | ')
    return {
        'title': title,
        'description': description
    }

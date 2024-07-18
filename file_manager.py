import abc
import json


class AbstractFileManager(abc.ABC):
    @abc.abstractmethod
    def write_to_file(self, task_list: list[dict]) -> None:
        pass

    @abc.abstractmethod
    def read_from_file(self) -> list[dict]:
        pass


class TextFileManager(AbstractFileManager):
    def __init__(self, filename):
        self._filename = filename

    def write_to_file(self, task_list: list[dict]) -> None:
        to_write = [self._format_task(task) for task in task_list]

        with open(self._filename, "w", encoding="utf-8") as f:
            f.write("\n".join(to_write))

    def read_from_file(self) -> list[dict]:
        task_list = []
        try:
            with open(self._filename, 'r', encoding='utf-8') as file:
                for line in file:
                    task_list.append(self._parse_str(line))
        except:
            pass
        return task_list

    def _format_task(self, task: dict) -> str:
        return f'{task["title"]} | {task["description"]}'

    def _parse_str(self, s: str) -> dict:
        title, description = s.strip().split(' | ')
        return {
            'title': title,
            'description': description
        }


class JSONFileManager(AbstractFileManager):
    def __init__(self, filename):
        self._filename = filename

    def write_to_file(self, task_list: list[dict]) -> None:
        with open(self._filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(task_list))

    def read_from_file(self) -> list[dict]:
        try:
            with open(self._filename, 'r', encoding='utf-8') as f:
                tasks = json.loads(f.read())
        except:
            tasks = []
        return tasks

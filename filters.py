class Command:
    def __init__(self, name):
        self._name = name

    def check(self, message: str):
        return message == f'/{self._name}'

    def __str__(self):
        return f'/{self._name}'


class CommandWithParams:
    def __init__(self, name):
        self._name = name

    def check(self, message: str):
        return message.startswith(f'/{self._name} ')

    def __str__(self):
        return f'/{self._name} <params>'


if __name__ == '__main__':
    f = Command('create') # /create
    print(f)
    print(f.check('/create'))
    print(f.check('/create asd'))
    print(f.check('/createasdsad'))

"""
self._name: "help"

s: "/helpasdasd"  == "/help"

"""

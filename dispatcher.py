class Dispatcher:
    def __init__(self):
        self._commands = {}

    def handle_message(self, message, description):
        def decorator(func):
            self._commands[message] = {'func': func, "description": description}
            return func

        return decorator

    def run(self):
        commands_descriptions = get_commands_list(self._commands)
        menu = f"Оберіть дію: \n{commands_descriptions}"
        while True:
            cmd = input(menu)
            if not cmd:
                break

            if cmd in self._commands:
                self._commands[cmd]['func']()
            else:
                print('Невірна команда!')


def get_commands_list(cmds):
    lines = []
    for key, value in cmds.items():
        lines.append(f'{key}. {value['description']}')

    return "\n".join(lines)

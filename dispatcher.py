class Dispatcher:
    def __init__(self):
        self._handlers = []

    def handle_message(self, filter_, description):
        def decorator(func):
            self._handlers.append({'func': func, "description": description, 'filter': filter_})
            return func

        return decorator

    def run(self):
        commands_descriptions = get_commands_list(self._handlers)
        menu = f"Оберіть дію: \n{commands_descriptions}\n"
        while True:
            cmd = input(menu)
            if not cmd:
                break

            for handler in self._handlers:
                if handler['filter'].check(cmd):
                    handler['func'](cmd)
                    break
            else:
                print('Невірна команда!')


def get_commands_list(handlers):
    lines = []
    for item in handlers:
        lines.append(f'{item['filter']} - {item['description']}')

    return "\n".join(lines)

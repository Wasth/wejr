class Router:
    def __init__(self):
        self._handlers = {}

    def method(self, func):
        self._handlers[func.__name__] = func
        return func

    def get_handler(self, name: str):
        return self._handlers.get(name)

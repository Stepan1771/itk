

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in type(cls)._instances:
            type(cls)._instances[cls] = super().__call__(*args, **kwargs)
        return type(cls)._instances[cls]



class Box(metaclass=SingletonMeta):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items


f = Box()
g = Box()
f.add_item("book")
print(g.get_items())


class SingletonNew:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls) # or object.__new__(cls)
        return cls.__instance

class MadCar(SingletonNew):
    def __init__(self):
        self.spares = []

    def add_spare(self, spare):
        self.spares.append(spare)

    def get_spares(self):
        return self.spares

c = MadCar()
d = MadCar()
c.add_spare("variator")
print(d.get_spares())
print(c is d)


class _SingletonWrapper:
    def __init__(self, cls):
        self.__wrapped__ = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self.__wrapped__(*args, **kwargs)
        return self._instance

def singleton(cls):
    return _SingletonWrapper(cls)


@singleton
class Dog:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def get_commands(self):
        return self.commands


a = Dog()
b = Dog()
a.add_command("sit down")
print(b.get_commands())
print(a is b)
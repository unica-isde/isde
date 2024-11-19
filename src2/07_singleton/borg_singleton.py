class Borg1:

    _shared_state: dict = {}  # Class attribute to hold shared state

    def __init__(self, x: int) -> None:
        self.__dict__ = self._shared_state
        self.x = x


class Borg2:

    _shared_state: dict = {}  # Class attribute to hold shared state

    def __new__(cls, *args, **kwargs) -> "Borg2":
        obj = super().__new__(cls)
        obj.__dict__ = cls._shared_state
        return obj

    def __init__(self, x: int) -> None:
        self.x = x


if __name__ == "__main__":
    borg1 = Borg2(10)
    print("borg1 ->", hex(id(borg1)))

    borg2 = Borg2(20)
    print("borg2 ->", hex(id(borg2)))

    print(borg1.x, borg2.x)
    print("__dict__ address:", hex(id(borg1.__dict__)), hex(id(borg2.__dict__)))

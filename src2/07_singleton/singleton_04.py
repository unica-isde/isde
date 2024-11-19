from typing import Any


class MetaSingleton(type):

    _dict_of_instances: dict = dict()

    def __call__(cls, *args, **kwargs) -> Any:
        if cls not in cls._dict_of_instances:
            cls._dict_of_instances[cls] = super().__call__(*args, **kwargs)
        return cls._dict_of_instances[cls]


class Singleton(metaclass=MetaSingleton):

    def __init__(self, x: str) -> None:
        self.x = x


class SingletonSubclass(Singleton, metaclass=MetaSingleton):
    pass


if __name__ == "__main__":
    s1 = Singleton("first value")
    print("s1 ->", hex(id(s1)))

    s2 = Singleton("second value")
    print("s2 ->", hex(id(s2)))
    print(s1.x, s2.x)

    s3 = SingletonSubclass("third value")
    print("s3 ->", hex(id(s3)))
    print(s3.x)

class Singleton:

    def __init__(self, x: str) -> None:
        self.x = x

    def __new__(cls, *args, **kwargs) -> None:
        if not hasattr(cls, "_instance"):
            print("1st call")
            cls._instance = super().__new__(cls)
        else:
            print("already exists")
        return cls._instance


if __name__ == "__main__":
    s1 = Singleton("first value")
    print("s1 ->", hex(id(s1)))

    s2 = Singleton("second value")
    print("s2 ->", hex(id(s2)))

    print(s1.x, s2.x)
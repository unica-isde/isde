
class Singleton:

    _instance: "Singleton" = None

    def __init__(self) -> None:
        raise RuntimeError("You cannot use the public constructor,"
                           "call `get_instance` instead")

    def _init(self) -> None:
        # initialize the object
        pass

    @staticmethod
    def get_instance() -> "Singleton":
        if Singleton._instance is None:
            Singleton._instance = Singleton.__new__(Singleton)
            Singleton._instance._init()
        return Singleton._instance


if __name__ == "__main__":
    s1 = Singleton.get_instance()
    print("s1 ->", hex(id(s1)))

    s2 = Singleton.get_instance()
    print("s2 ->", hex(id(s2)))

    s3 = Singleton()

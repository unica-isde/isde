class SomeClass:

    def method_1(self):
        print("original method_1 of SomeClass")

    def method_2(self):
        print("original method_2 of SomeClass")


class Decorator:

    def __init__(self, obj):
        self._obj = obj

    def method_1(self):
        print("decorator operation")
        self._obj.method_1()

    def __getattr__(self, item):
        return getattr(self._obj, item)


if __name__ == "__main__":
    obj = SomeClass()
    obj.method_1()

    wrapped_obj = Decorator(obj)
    wrapped_obj.method_1()
    wrapped_obj.method_2()

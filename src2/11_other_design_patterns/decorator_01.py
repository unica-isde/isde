class SomeClass:

    def method_1(self):
        print("original method_of SomeClass")


class DecoratorClass:

    def __init__(self, obj):
        self._obj = obj

    def method_1(self):
        print("decorator operations")
        self._obj.method_1()


if __name__ == "__main__":
    obj = SomeClass()
    obj.method_1()

    wrapped_obj = DecoratorClass(obj)
    wrapped_obj.method_1()

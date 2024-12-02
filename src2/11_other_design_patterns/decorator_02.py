from abc import ABC, abstractmethod


class AbstractSomeClass(ABC):

    @abstractmethod
    def method_1(self):
        pass

    @abstractmethod
    def method_2(self):
        pass


class SomeClass(AbstractSomeClass):

    def method_1(self):
        print("original method_1 of SomeClass")

    def method_2(self):
        print("original method_2 of SomeClass")


class BaseDecorator(AbstractSomeClass):

    def __init__(self, obj):
        self._obj = obj

    def method_1(self):
        self._obj.method_1()

    def method_2(self):
        self._obj.method_2()


class Decorator(BaseDecorator):

    def method_1(self):
        print("decorator operation")
        self._obj.method_1()


if __name__ == "__main__":
    obj = SomeClass()
    obj.method_1()

    wrapped_obj = Decorator(obj)
    wrapped_obj.method_1()
    wrapped_obj.method_2()

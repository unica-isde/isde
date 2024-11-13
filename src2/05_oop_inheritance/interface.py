from abc import ABC, abstractmethod


class Character(ABC):

    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    def fight(self):
        pass

    @abstractmethod
    def jump(self):
        pass

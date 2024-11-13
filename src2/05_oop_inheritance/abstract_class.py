from abc import ABC, abstractmethod


class Character(ABC):

    def __init__(self, name):
        self.name = name
        self.score = 0

    def fight(self):
        print("THIS IS SPARTA!")

    @abstractmethod
    def jump(self):  # you are forced to redefine this method
        print("JUMP!")


class Mouse(Character):

    def jump(self):
        super().jump()
        print("A mouse can jump!")


class Kangaroo(Character):

    def jump(self):
        super().jump()
        print("A kangaroo can jump very high!")


if __name__ == "__main__":
    Mouse("Mickey Mouse").jump()
    Kangaroo("a_Kangaroo").jump()

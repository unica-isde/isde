from abc import ABC, abstractmethod


class Bird(ABC):

    @abstractmethod
    def fly(self):
        pass


class Sparrow(Bird):
    def fly(self):
        print("I can fly!")


class Penguin(Bird):
    def fly(self):
        # Penguins cannot fly, so this violates LSP
        raise ValueError("I can't fly!")


if __name__ == "__main__":
    # Function that takes a Bird and expects it to fly
    def make_bird_fly(bird):
        bird.fly()


    b1 = Sparrow()
    b2 = Penguin()
    list_of_birds = [b1, b2]
    for el in list_of_birds:
        make_bird_fly(el)  # Raises ValueError: "I can't fly!"

from abc import ABC, abstractmethod 


class Bird(ABC):
  pass


class FlyingBird(ABC):

  def fly(self):
    print("I can fly!")


class Sparrow(FlyingBird):
  pass

class Penguin(Bird):
  pass


if __name__ == "__main__":
    def make_bird_fly(bird):
      bird.fly()


    fb1 = Sparrow()
    fb2 = Sparrow()
    list_of_birds = [fb1, fb2]
    for el in list_of_birds:
      make_bird_fly(el)

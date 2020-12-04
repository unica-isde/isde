from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def fight_against(self, other_weapon):
        pass

    def __str__(self):
        return self.__class__.__name__


class Scissor(Weapon):
    def fight_against(self, other_weapon):
        if type(other_weapon) is Scissor:
            return "TIE"
        elif type(other_weapon) is Paper:
            return "Scissor"
        else:
            return "Rock"


class Rock(Weapon):
    def fight_against(self, other_weapon):
        if type(other_weapon) is Rock:
            return "TIE"
        elif type(other_weapon) is Paper:
            return "Paper"
        else:
            return "Rock"


class Paper(Weapon):
    def fight_against(self, other_weapon):
        if type(other_weapon) is Paper:
            return "TIE"
        elif type(other_weapon) is Rock:
            return "Paper"
        else:
            return "Scissor"


if __name__ == '__main__':
    print("\n\n")
    list_of_weapons = [Scissor(), Paper(), Rock()]
    for w1 in list_of_weapons:
        for w2 in list_of_weapons:
            print(w1, 'vs', w2, '->', w1.fight_against(w2))

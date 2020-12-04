from abc import ABC, abstractmethod


class Weapon(ABC):

    def __str__(self):
        return self.__class__.__name__

    @abstractmethod
    def fight_against(self, other_weapon):
        pass

    # second dispatch
    @abstractmethod
    def _fight_against_scissor(self):
        pass

    @abstractmethod
    def _fight_against_rock(self):
        pass

    @abstractmethod
    def _fight_against_paper(self):
        pass


class Scissor(Weapon):
    def fight_against(self, other_weapon):
        # dear other_weapon, I am a Scissor object!
        # I don't know who are you,
        # BUT YOU KNOW WHO ARE YOU and WHO I AM
        return other_weapon._fight_against_scissor()

    # second dispatch
    def _fight_against_scissor(self):
        return "TIE"

    def _fight_against_rock(self):
        return "Rock"

    def _fight_against_paper(self):
        return "Scissor"


class Rock(Weapon):
    def fight_against(self, other_weapon):
        return other_weapon._fight_against_rock()

    # second dispatch
    def _fight_against_scissor(self):
        return "Rock"

    def _fight_against_rock(self):
        return "TIE"

    def _fight_against_paper(self):
        return "Paper"


class Paper(Weapon):
    def fight_against(self, other_weapon):
        return other_weapon._fight_against_paper()

    # second dispatch
    def _fight_against_scissor(self):
        return "Scissor"

    def _fight_against_rock(self):
        return "Paper"

    def _fight_against_paper(self):
        return "TIE"


if __name__ == '__main__':
    print("\n\n")

    list_of_weapons = [Scissor(), Paper(), Rock()]
    for w1 in list_of_weapons:
        for w2 in list_of_weapons:
            print(w1, 'vs', w2, '->', w1.fight_against(w2))
    print("\n\n")

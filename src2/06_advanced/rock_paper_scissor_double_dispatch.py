from abc import ABC, abstractmethod


class Weapon(ABC):

    def __str__(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def fight_against(
            self,
            other_weapon: "Weapon"
    ) -> str:
        pass

    # second dispatch
    @abstractmethod
    def _fight_against_scissor(self) -> str:
        pass

    @abstractmethod
    def _fight_against_rock(self) -> str:
        pass

    @abstractmethod
    def _fight_against_paper(self) -> str:
        pass


class Scissor(Weapon):

    def fight_against(
            self,
            other_weapon: "Weapon"
    ) -> str:
        # dear other_weapon, I am a Scissor object!
        # I don't know who are you,
        # BUT YOU KNOW WHO ARE YOU and WHO I AM
        return other_weapon._fight_against_scissor()

    # second dispatch
    def _fight_against_scissor(self) -> str:
        return "TIE"

    def _fight_against_rock(self) -> str:
        return "Rock"

    def _fight_against_paper(self) -> str:
        return "Scissor"


class Rock(Weapon):

    def fight_against(
            self,
            other_weapon: "Weapon"
    ) -> str:
        return other_weapon._fight_against_rock()

    # second dispatch
    def _fight_against_scissor(self) -> str:
        return "Rock"

    def _fight_against_rock(self) -> str:
        return "TIE"

    def _fight_against_paper(self) -> str:
        return "Paper"


class Paper(Weapon):

    def fight_against(
            self,
            other_weapon: "Weapon"
    ) -> str:
        return other_weapon._fight_against_paper()

    # second dispatch
    def _fight_against_scissor(self) -> str:
        return "Scissor"

    def _fight_against_rock(self) -> str:
        return "Paper"

    def _fight_against_paper(self) -> str:
        return "TIE"


if __name__ == "__main__":
    list_of_weapons = [Scissor(), Paper(), Rock()]
    for w1 in list_of_weapons:
        for w2 in list_of_weapons:
            print(w1, "vs", w2, "->", w1.fight_against(w2))

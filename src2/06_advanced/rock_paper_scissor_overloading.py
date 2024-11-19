from abc import ABC, abstractmethod
from plum import dispatch


class Weapon(ABC):

    def __str__(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    @dispatch
    def fight_against(
            self,
            other_weapon: "Scissor"
    ) -> str:
        pass

    @abstractmethod
    @dispatch
    def fight_against(
            self,
            other_weapon: "Rock"
    ) -> str:
        pass

    @abstractmethod
    @dispatch
    def fight_against(
            self,
            other_weapon: "Paper"
    ) -> str:
        pass


class Scissor(Weapon):

    @dispatch
    def fight_against(
            self,
            other_weapon: "Scissor"
    ) -> str:
        return "TIE"

    @dispatch
    def fight_against(
            self,
            other_weapon: "Rock"
    ) -> str:
        return "Rock"

    @dispatch
    def fight_against(
            self,
            other_weapon: "Paper"
    ) -> str:
        return "Scissor"


class Paper(Weapon):

    @dispatch
    def fight_against(
            self,
            other_weapon: "Scissor"
    ) -> str:
        return "Scissor"

    @dispatch
    def fight_against(
            self,
            other_weapon: "Rock"
    ) -> str:
        return "Paper"

    @dispatch
    def fight_against(
            self,
            other_weapon: "Paper"
    ) -> str:
        return "TIE"


class Rock(Weapon):

    @dispatch
    def fight_against(
            self,
            other_weapon: "Scissor"
    ) -> str:
        return "Rock"

    @dispatch
    def fight_against(
            self,
            other_weapon: "Rock"
    ) -> str:
        return "TIE"

    @dispatch
    def fight_against(
            self,
            other_weapon: "Paper"
    ) -> str:
        return "Paper"


if __name__ == "__main__":
    list_of_weapons = [Scissor(), Paper(), Rock()]
    for w1 in list_of_weapons:
        for w2 in list_of_weapons:
            print(w1, "vs", w2, "->", w1.fight_against(w2))

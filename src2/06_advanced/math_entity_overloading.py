from abc import ABC, abstractmethod
from plum import dispatch


class MathEntity(ABC):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    @dispatch
    def __add__(self, op2: "R") -> "MathEntity":
        pass

    @abstractmethod
    @dispatch
    def __add__(self, op2: "C") -> "C":
        pass


class R(MathEntity):

    def __init__(self, re) -> None:
        self.re = re

    def __repr__(self) -> str:
        return str(self.re)

    @dispatch
    def __add__(self, op2: "R") -> "R":
        return R(self.re + op2.re)

    @dispatch
    def __add__(self, op2: "C") -> "C":
        return C(self.re + op2.re, op2.img)


class C(MathEntity):
    """represents re + i img """

    def __init__(self, re, img=0) -> None:
        self.re = re
        self.img = img

    def __repr__(self) -> str:
        s_sign = ["-", "+"][self.img > 0]
        s_img = "" if self.img == 0 else s_sign + "i" + str(abs(self.img))
        return str(self.re) + s_img

    @dispatch
    def __add__(self, op2: "R") -> "C":
        return C(self.re + op2.re, self.img)

    @dispatch
    def __add__(self, op2: "C") -> "C":
        return C(self.re + op2.re, self.img + op2.img)


if __name__ == "__main__":
    values = [R(2), R(-3), C(2, 3), C(3, -3)]
    for op1 in values:
        for op2 in values:
            print(op1, "+", op2, "=", op1 + op2)

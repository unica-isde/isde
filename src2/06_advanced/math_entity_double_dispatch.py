from abc import ABC, abstractmethod


class MathEntity(ABC):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: "MathEntity") -> "MathEntity":
        pass

    @abstractmethod
    def _add_real(self, op1: "R") -> "MathEntity":
        pass

    @abstractmethod
    def _add_complex(self, op1: "C") -> "C":
        pass


class R(MathEntity):

    def __init__(self, re: int) -> None:
        self.re = re

    def __repr__(self) -> str:
        return str(self.re)

    def __add__(self, op2: "MathEntity") -> "MathEntity":
        return op2._add_real(self)

    def _add_real(self, op1: "R") -> "R":
        return R(self.re + op1.re)

    def _add_complex(self, op1: "C") -> "C":
        return C(self.re + op1.re, op1.img)


class C(MathEntity):
    """represents re + i img """

    def __init__(self, re, img=0) -> None:
        self.re = re
        self.img = img

    def __repr__(self) -> str:
        s_sign = ["-", "+"][self.img > 0]
        s_img = "" if self.img == 0 else s_sign + "i" + str(abs(self.img))
        return str(self.re) + s_img

    def __add__(self, op2: "MathEntity") -> "MathEntity":
        return op2._add_complex(self)

    def _add_real(self, op1: "R") -> "C":
        return C(self.re + op1.re, self.img)

    def _add_complex(self, op1: "C") -> "C":
        return C(self.re + op1.re, self.img + op1.img)


if __name__ == "__main__":
    values = [R(2), R(-3), C(2, 3), C(3, -3)]
    for op1 in values:
        for op2 in values:
            print(op1, "+", op2, "=", op1 + op2)

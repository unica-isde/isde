from typing import Sequence

class AlternateListComp:

    def __init__(
            self
    ) -> None:
        self._values: list = []
        self._accept: bool = True

    def add_item(
            self,
            v: int
    ) -> None:
        if self._accept:
            self._values.append(v)
        self._accept = not self._accept

    def add_collection(
            self,
            v_collection: Sequence[int]
    ) -> None:
        for v in v_collection:
            self.add_item(v)

    def __str__(
            self
    ) -> str:
        return str(self._values)


if __name__ == "__main__":
    n = 21
    obj_comp = AlternateListComp()
    for i in range(1, n):
        obj_comp.add_item(i)
    print(obj_comp)

    obj_comp = AlternateListComp()
    obj_comp.add_collection(list(range(1, n)))

    print(obj_comp)

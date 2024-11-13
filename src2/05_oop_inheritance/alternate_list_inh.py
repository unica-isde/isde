from typing import Sequence


class AlternateListInh(list):

    def __init__(
            self,
            *args,
            **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self._accept: bool = True

    def add_item(
            self,
            v: int
    ) -> None:
        if self._accept:
            self.append(v)
        self._accept = not self._accept

    def add_collection(
            self,
            v_collection: Sequence[int]
    ) -> None:
        for v in v_collection:
            self.add_item(v)


if __name__ == "__main__":
    n = 21
    obj_inh = AlternateListInh()
    for i in range(1, n):
        obj_inh.add_item(i)
    print(obj_inh)

    obj_inh = AlternateListInh()
    obj_inh.add_collection(list(range(1, n)))

    print(obj_inh)

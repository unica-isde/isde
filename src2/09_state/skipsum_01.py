class SumSkip:

    def __init__(self, el_to_skip: int) -> None:
        self.el_to_skip = el_to_skip
        self._state: int = 0
        self.sum_val: int = 0

    def sum_skip_el(self, el: int) -> None:
        if self._state == 0:
            if el == self.el_to_skip:
                self._state = 1
            else:
                self.sum_val += el
        elif self._state == 1:
            if el == self.el_to_skip:
                pass
            else:
                self._state = 0

    def reset(self) -> None:
        self.__init__(self.el_to_skip)


if __name__ == "__main__":
    nums1 = [1, 13, 10, 1, 13, 13, 13, 10, 1, 13]
    nums2 = [1, 13, 10, 1, 13, 13, 13, 10, 1]
    nums3 = [13, 10, 1, 13, 13, 13, 10, 1]

    list_of_nums = [nums1, nums2, nums3]
    list_of_results = [3, 3, 2]
    obj = SumSkip(13)

    for nums, r in zip(list_of_nums, list_of_results):
        for el in nums:
            obj.sum_skip_el(el)
        print(obj.sum_val == r)
        obj.reset()

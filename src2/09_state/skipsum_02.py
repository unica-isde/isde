class SkipWithState:

    def __init__(self, el_to_skip: int, start_state: int = 0) -> None:
        self.el_to_skip = el_to_skip
        self.sum_val: int = 0
        self._state = start_state
        self._transition_table = {
            0: {
                el_to_skip: {"action": self.f_null, "next_state": 1},
                "default_input": {"action": self.f_sum, "next_state": 0}
            },
            1: {
                el_to_skip: {"action": self.f_null, "next_state": 1},
                "default_input": {"action": self.f_null, "next_state": 0}
            }
        }

    def f_null(self, v: int) -> None:
        pass

    def f_sum(self, v: int) -> None:
        self.sum_val += v

    def process_input(self, v_input: int) -> None:
        actual_transition_table = self._transition_table[self._state]
        if v_input in actual_transition_table:
            action = actual_transition_table[v_input]["action"]
            next_state = actual_transition_table[v_input]["next_state"]
        else:
            action = actual_transition_table["default_input"]["action"]
            next_state = actual_transition_table["default_input"]["next_state"]
        action(v_input)
        self._state = next_state

    def reset(self) -> None:
        self.__init__(self.el_to_skip)


if __name__ == "__main__":
    nums1 = [1, 13, 10, 1, 13, 13, 13, 10, 1, 13]
    nums2 = [1, 13, 10, 1, 13, 13, 13, 10, 1]
    nums3 = [13, 10, 1, 13, 13, 13, 10, 1]

    list_of_nums = [nums1, nums2, nums3]
    list_of_results = [3, 3, 2]
    obj = SkipWithState(13)

    for nums, r in zip(list_of_nums, list_of_results):
        for el in nums:
            obj.process_input(el)
        print(obj.sum_val == r)
        obj.reset()

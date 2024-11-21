from abc import ABC, abstractmethod


class State(ABC):

    def process_input(self, context, v):
        self._action(context, v)
        self._change_state(context, v)

    @abstractmethod
    def _action(self, context, v):
        pass

    @abstractmethod
    def _change_state(self, context, v):
        pass


class StateSum(State):

    def _action(self, context, v):
        if v != context.value_to_skip:
            context.sum(v)

    def _change_state(self, context, v):
        if v == context.value_to_skip:
            context.set_state(StateSkip())


class StateSkip(State):

    def _action(self, context, v):
        pass

    def _change_state(self, context, v):
        if v != context.value_to_skip:
            context.set_state(StateSum())


class SumSkip:

    def __init__(self, value_to_skip):
        self._state = StateSum()
        self.sum_val = 0
        self.value_to_skip = value_to_skip

    def set_state(self, state):
        self._state = state

    def process_input(self, v):
        self._state.process_input(self, v)

    def sum(self, v):
        self.sum_val += v


if __name__ == "__main__":
    nums1 = [1, 13, 10, 1, 13, 13, 13, 10, 1, 13]
    nums2 = [1, 13, 10, 1, 13, 13, 13, 10, 1]
    nums3 = [13, 10, 1, 13, 13, 13, 10, 1]

    list_of_nums = [nums1, nums2, nums3]
    list_of_results = [3, 3, 2]

    for nums, r in zip(list_of_nums, list_of_results):
        s = SumSkip(13)
        for el in nums:
            s.process_input(el)
        print(s.sum_val == r)

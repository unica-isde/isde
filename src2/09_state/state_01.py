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
        context.sum(v)

    def _change_state(self, context, v):
        context.set_state(StateSkip())


class StateSkip(State):

    def _action(self, context, v):
        pass

    def _change_state(self, context, v):
        context.set_state(StateSum())


class SumSkip:

    def __init__(self):
        self._state = StateSum()
        self.sum_val = 0

    def set_state(self, state):
        self._state = state

    def process_input(self, v):
        self._state.process_input(self, v)

    def sum(self, v):
        self.sum_val += v


if __name__ == "__main__":
    n = 10
    values = list(range(n))
    correct_sum = sum(range(0, n, 2))

    s = SumSkip()
    for el in values:
        s.process_input(el)

    print(s.sum_val == correct_sum)

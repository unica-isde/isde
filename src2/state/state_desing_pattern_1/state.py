from abc import ABC, abstractmethod


class State(ABC):

    def process_input(self, adder, v):
        """ the implementation is in the superclass method because in this specific problem
        the instruction flow is 'ACTION'->'CHANGE STATE' for all the (state, input)
        otherwise you can define process_input as an abstract method and implement it in subclasses. """
        self._action(adder, v)
        self._change_state(adder, v)

    @abstractmethod
    def _action(self, adder, v):
        pass

    @abstractmethod
    def _change_state(self, adder, v):
        pass


class StateSum(State):

    def _action(self, adder, v):
        # who should perform the 'sum'?
        adder.sum_val += v
        # adder.sum(v)

    def _change_state(self, adder, v):
        adder.set_state(StateSkip())


class StateSkip(State):

    def _action(self, adder, v):
        pass

    def _change_state(self, adder, v):
        adder.set_state(StateSum())

from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def get_actual_price(self, value):
        pass  # DO NOTHING

    @abstractmethod
    def get_actual_dress(self):
        pass  # DO NOTHING


class NormalStrategy(Strategy):
    def get_actual_price(self, value):
        return value

    def get_actual_dress(self):
        print('normal dress')


class HappyHourStrategy(Strategy):
    def get_actual_price(self, value):
        # (50 % discount)
        return value * 0.5

    def get_actual_dress(self):
        print('happy hour dress')

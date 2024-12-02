from typing import Dict, Callable


class Subscriber:

    def __init__(self, name: str) -> None:
        self.name = name

    def it_is_increasing(self, message: str) -> None:
        print(self.name,
              " (`it_is_increasing` method) received the message ",
              message)

    def it_is_decreasing(self, message: str) -> None:
        print(self.name,
              " (`it_is_decreasing` method) received the message ",
              message)


class Publisher:
    default_method_name = "update"
    events = ["decrease", "increase"]

    def __init__(self, x: int) -> None:
        self._subscribers: Dict[str : Dict[Subscriber: Callable]] = {
            event: dict() for event in self.events}
        self._x = x

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x: int) -> None:
        if not hasattr(self, "_x"):
            # first assignment
            self._x = x
        else:
            if self._x != x:
                # update subscribers
                event = self.events[x > self._x]
                self._x = x
                message = f"The new value of x is {x}"
                self.dispatch(event, message)

    def register(
            self,
            event: str,
            subscriber: Subscriber,
            method_to_invoke: Callable = None
    ) -> None:
        if method_to_invoke is None:
            method_to_invoke = getattr(subscriber, self.default_method_name)
        self._subscribers[event][subscriber] = method_to_invoke

    def unregister(self, event: str, subscriber) -> None:
        if subscriber in self._subscribers[event]:
            del self._subscribers[event][subscriber]

    def dispatch(self, event: str, message: str) -> None:
        for method_to_invoke in self._subscribers[event].values():
            method_to_invoke(message)


if __name__ == "__main__":
    # client code 004
    obs1 = Subscriber("obs1")
    obs2 = Subscriber("obs2")
    publisher = Publisher(0)

    # obs1, obs2 are interested in the publisher's state
    # obs1  uses the `it_is_increasing()` method and
    #  it is interested on events 'increase'
    publisher.register("increase", obs1, obs1.it_is_increasing)

    # obs2 uses  the `it_is_decreasing()` method and
    #  it is interested on event 'decrease'
    publisher.register("decrease", obs2, obs2.it_is_decreasing)

    print("# 1 - x increase. Message from obs1")
    publisher.x = 10

    print("\n# 2 - x decrease. Message from obs2")
    publisher.x = 5

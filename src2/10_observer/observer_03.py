from typing import Dict, Callable, List


class Subscriber:

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, message: str) -> None:
        print(self.name, " (update method) received the message", message)

    def receive(self, message: str) -> None:
        print(self.name, " (receive method) received the message", message)


class Publisher:

    default_method_name = "update"

    def __init__(self, events: List[str], x: int, y: int) -> None:
        self.x = x
        self.y = y
        self._subscribers: Dict[str : Dict[Subscriber: Callable]] = {
            event: dict() for event in events}

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
                # udpate subscribers
                self._x = x
                message = f"The new value of x is {x}"
                self.dispatch("x", message)

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, y: int) -> None:
        if not hasattr(self, "_y"):
            # first assignment
            self._y = y
        else:
            if self._y != y:
                # udpate subscribers
                self._y = y
                message = f"The new value of y is {y}"
                self.dispatch("y", message)

    def dispatch(self, event:str, message: str) -> None:
        for method_to_invoke in self._subscribers[event].values():
            method_to_invoke(message)

    def register(
            self,
            event: str,
            subscriber: Subscriber,
            method_to_invoke: Callable = None
    ) -> None:
        if method_to_invoke is None:
            method_to_invoke = getattr(subscriber, self.default_method_name)
        self._subscribers[event][subscriber] = method_to_invoke

    def unregister(self, event: str, subscriber: Subscriber) -> None:
        if subscriber in self._subscribers:
            del self._subscribers[event][subscriber]


if __name__ == "__main__":
    # client code 003
    obs1 = Subscriber("obs1")
    obs2 = Subscriber("obs2")
    publisher = Publisher(["x", "y"], 0,
                          0)  # it accepts in input a list of events

    # obs1, obs2 are interested in the publisher's state
    # obs1 implicitly uses the `update()` method and it is interested on events 'x changes' and 'y changes'
    publisher.register("x", obs1)
    publisher.register("y", obs1)

    # obs2 explicitly indicate the `receive()` method and it is interested on event 'y changes'
    publisher.register("y", obs2, obs2.receive)

    print("# 1 - x changes. Message from obs1")
    publisher.x = 10

    print("\n# 2 - y changes. Message from obs1 and obs2 ")
    publisher.y = 20

    print("\n# 3 - no message")  # obs1 is no longer interested in 'x'
    publisher.unregister("x", obs1)
    publisher.x = 11  # NO MESSAGE

    print("\n# 4 - y changes. Message from obs1 and obs2 ")
    publisher.y = 30

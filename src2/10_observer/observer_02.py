from typing import Dict, Callable


class Subscriber:

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, message: str) -> None:
        print(self.name, " (update method) received the message", message)

    def receive(self, message: str) -> None:
        print(self.name, " (receive method) received the message", message)


class Publisher:

    default_method_name = "update"

    def __init__(self, x: int) -> None:
        self.x = x
        self._subscribers: Dict[Subscriber: Callable] = dict()

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
                self._x = x
                message = f"The new value of x is {x}"
                self.dispatch(message)

    def dispatch(self, message: str) -> None:
        for method_to_invoke in self._subscribers.values():
            method_to_invoke(message)

    def register(self, subscriber: Subscriber, method_to_invoke: Callable = None) -> None:
        if method_to_invoke is None:
            method_to_invoke = getattr(subscriber, self.default_method_name)
        self._subscribers[subscriber] = method_to_invoke

    def unregister(self, subscriber: Subscriber) -> None:
        if subscriber in self._subscribers:
            del self._subscribers[subscriber]


if __name__ == "__main__":
    # client code 002
    obs1 = Subscriber("obs1")
    obs2 = Subscriber("obs2")
    publisher = Publisher(0)

    # obs1, obs2 are interested in the publisher's state
    # obs1 implicitly uses the `update()` method
    # obs2 explicitly indicate the `receive()` method
    publisher.register(obs1)
    publisher.register(obs2, obs2.receive)

    # x does not change. No message from observers
    publisher.x = 0
    # x changes. Message from obs1, obs2
    publisher.x = 10
    # obs1 is no longer interested in the publisher's state.
    publisher.unregister(obs1)
    # x changes. Message from obs2 only
    publisher.x = 20

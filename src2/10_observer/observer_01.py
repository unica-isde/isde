from typing import Set


class Subscriber:

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, message: str) -> None:
        print(self.name, " received the message", message)


class Publisher:

    def __init__(self, x: int) -> None:
        self.x = x
        self._subscribers: Set[Subscriber] = set()

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
        for subscriber in self._subscribers:
            subscriber.update(message)

    def register(self, subscriber: Subscriber) -> None:
        self._subscribers.add(subscriber)

    def unregister(self, subscriber: Subscriber) -> None:
        self._subscribers.remove(subscriber)

if __name__ == "__main__":
    # client code 001
    obs1 = Subscriber("obs1")
    obs2 = Subscriber("obs2")
    obs3 = Subscriber("obs3")
    publisher = Publisher(0)

    # obs1, obs2 are interested in the publisher's state
    publisher.register(obs1)
    publisher.register(obs2)

    # x does not change. No message from the observers
    publisher.x = 0

    # x changes. Message from obs1, obs2
    publisher.x = 10

    # obs1 is no longer interested in the publisher's state.
    publisher.unregister(obs1)

    # x changes. Message from obs2 only
    publisher.x = 20

# observer1.py
# The Observer
class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(self.name, ' received the message ', message)


# The Observable
class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, an_observer):
        self.subscribers.add(an_observer)

    def unregister(self, an_observer):
        self.subscribers.discard(an_observer)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


# driver

publisher = Publisher()  # the observed object
bob = Subscriber('Bob')  # an observer
alice = Subscriber('Alice')  # an observer
john = Subscriber('John')  # an observer

# add the observers to the subscribers' set of the publisher
publisher.register(bob)
publisher.register(alice)
publisher.register(john)

# please note that a subscriber can register itself by calling `publisher.register(self)`

# send a message
publisher.dispatch('Lunchtime!')

print("\n")
publisher.unregister(john)
publisher.dispatch('Happy hour!')

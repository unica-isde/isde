# observer2.py

# The Observer
class SubscriberOne:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(self.name, ' (update method) received the message ', message)


# The Observer
class SubscriberTwo:
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print(self.name, ' (receive method) received the message ', message)


# The Observable
class Publisher:
    def __init__(self):
        self.subscribers = dict()  # set()
        # subscribers is a dictionary.
        #  key: an_observer
        #  value: the 'update' method or others.

    def register(self, an_observer, callback=None):
        default_method = 'update'
        if callback is None:
            # call the 'default' method
            callback = getattr(an_observer, default_method)
            # callback = an_observer.update
        self.subscribers[an_observer] = callback

    def unregister(self, an_observer):
        del self.subscribers[an_observer]

    def dispatch(self, message):
        for subscriber, callback in self.subscribers.items():
            # returns all "key, value" couples
            callback(message)


# driver

publisher = Publisher()

bob = SubscriberOne('Bob')  # has update() method
alice = SubscriberOne('Alice')  # has update() method
john = SubscriberTwo('John')  # has **receive()** method

publisher.register(bob, bob.update)  # explicitly uses the 'update()' method
publisher.register(alice)  # implicitly uses the 'update()' method
publisher.register(john, john.receive)  # explicitly uses the 'receive()' method

# send a message
publisher.dispatch('Lunchtime!')
print("\n")
publisher.unregister(john)
publisher.dispatch('Happy hour!')

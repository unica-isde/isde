# observer3.py  (Python 3)

# The Observer
#  In this example SubscriberOne uses the update method
#  and SubscriberTwo uses the receive method
#  But it is possible to have different methods for different events
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
    def __init__(self, events):
        # The constructor accepts in input a list of events
        # __init__ uses this list to initialize a dictionary
        self.subscribers = {event: dict() for event in events}

    def get_subscribers(self, event):  # helper method
        return self.subscribers[event]

    def register(self, event, an_observer, callback=None):
        default_method = 'update'
        if callback is None:
            # set the callback to the update method
            callback = getattr(an_observer, default_method)
        self.get_subscribers(event)[an_observer] = callback

    def unregister(self, event, an_observer):
        del self.get_subscribers(event)[an_observer]

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            # returns all "key, value" couples FOR THE DICTIONARY RELATED TO THIS EVENT
            callback(message)


# driver

# possible events are ('lunch', 'happyhour')
publisher = Publisher(['lunch', 'happyhour'])

bob = SubscriberOne('Bob')
alice = SubscriberOne('Alice')
john = SubscriberTwo('John')

# bob and john are interested in the event 'lunch'
publisher.register('lunch', bob)  # implicitly uses the 'update()' method
publisher.register('lunch', john, john.receive)  # explicitly uses the 'receive()' method

# alice and john are interested in the event 'happyhour'
publisher.register('happyhour', alice)  # implicitly uses the 'update()' method
publisher.register('happyhour', john, john.receive)  # explicitly uses the 'receive()' method

# send a message
print('\nLUNCHTIME!')
publisher.dispatch('lunch', 'Lunchtime!')  # event, message
print('\nHAPPYHOUR!')
publisher.dispatch('happyhour', 'HAPPY HOUR!')  # event, message

print("\nNow  john is no longer interested in event 'happyhour'")
print("but he remains interested in event 'lunch'\n")

publisher.unregister('happyhour', john)

# send a message
print('\nLUNCHTIME!')
publisher.dispatch('lunch', 'Lunchtime!')  # event, message
print('\nHAPPYHOUR!')
publisher.dispatch('happyhour', 'HAPPY HOUR!')  # event, message

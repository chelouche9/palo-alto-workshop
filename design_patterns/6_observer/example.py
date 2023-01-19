# Observer interface
class IObserver:
    def update(self, subject: object, *args, **kwargs):
        pass

# Subject class that publishes events
class Subject:
    def __init__(self):
        self._observers = []
    
    def register_observer(self, observer: IObserver):
        self._observers.append(observer)
    
    def unregister_observer(self, observer: IObserver):
        self._observers.remove(observer)
    
    def notify_observers(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(self, *args, **kwargs)

# Concrete observer class that receives events from the subject
class Observer1(IObserver):
    def update(self, subject: object, *args, **kwargs):
        print(f'Observer1 received event: {args}, {kwargs}')

# Another concrete observer class that receives events from the subject
class Observer2(IObserver):
    def update(self, subject: object, *args, **kwargs):
        print(f'Observer2 received event: {args}, {kwargs}')

# Create a Subject object
subject = Subject()

# Create two Observer objects
observer1 = Observer1()
observer2 = Observer2()

# Register the observers with the subject
subject.register_observer(observer1)
subject.register_observer(observer2)

# Notify the observers of an event
subject.notify_observers('event1', foo=1, bar=2)
# Output:
# Observer1 received event: ('event1',), {'foo': 1, 'bar': 2}
# Observer2 received event: ('event1',), {'foo': 1, 'bar': 2}

# Unregister one of the observers
subject.unregister_observer(observer1)

# Notify the observers of another event
subject.notify_observers('event2', foo=3, bar=4)
# Output:
# Observer2 received event: ('event2',), {'foo': 3, 'bar': 4}
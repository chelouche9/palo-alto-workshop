# Target interface
class ITarget:
    def request(self):
        pass

# Adaptee class with an incompatible interface
class Adaptee:
    def specific_request(self):
        print('Performing specific request...')

# Adapter class that adapts the Adaptee class to the Target interface
class Adapter(ITarget):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee
    
    def request(self):
        self.adaptee.specific_request()

# Create an Adaptee object
adaptee = Adaptee()

# Create an Adapter object and pass the Adaptee object as a dependency
adapter = Adapter(adaptee)

# Use the Adapter object
adapter.request()  # Output: Performing specific request...
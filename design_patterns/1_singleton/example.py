class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

class MyClass(Singleton):
    def __init__(self, value):
        self.value = value

# Create two instances of MyClass
a = MyClass(1)
b = MyClass(2)

# The instances are the same object
print(a is b)  # Output: True

# The value of the instance is the value of the last object created
print(a.value)  # Output: 2
print(b.value)  # Output: 2
# Animal interface
class Animal:
    def speak(self):
        pass

# Concrete animals
class Dog(Animal):
    def speak(self):
        print('Woof!')

class Cat(Animal):
    def speak(self):
        print('Meow!')

# Animal factory
class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()
        else:
            raise ValueError('Invalid animal type')

# Create an AnimalFactory object
factory = AnimalFactory()

# Create a dog using the factory
dog = factory.create_animal('dog')
dog.speak()  # Output: Woof!

# Create a cat using the factory
cat = factory.create_animal('cat')
cat.speak()  # Output: Meow!
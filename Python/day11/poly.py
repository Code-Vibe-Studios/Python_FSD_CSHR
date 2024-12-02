class Animal:
    def speak(self):
        return "Animal talks"


class Dog(Animal):
    def speak(self):
        return "barks"

class Cat(Animal):
    def speak(self):
        return "meow"

animal = Animal()
print(animal.speak())
dog = Dog()
print(dog.speak())
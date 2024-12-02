class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("This animal makes a sound")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} says Woof!")

denver = Dog("Denver","Golden Retriever")
denver.speak()

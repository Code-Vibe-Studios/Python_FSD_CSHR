class Car:
    def __init__(self,color,model):       # reference of the object self = myCar
        self.color = color                # self.color = myCar.color = color
        self.model = model
        print(f"{self} is created")

    def display(self):
        print(f"This car is a {self.color} {self.model}")

myCar = Car("silver","i20")
print(myCar.color)
# myCar.display()
# naveenCar = Car("red","audi")
# naveenCar.display()
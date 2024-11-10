class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class ElectricCar(Car):
    def charge(self):
        print("Charging the car")

eon = ElectricCar()
eon.start()
eon.drive()
eon.charge()


i20 = Car()
i20.start()
i20.drive()
from abc import ABC,abstractmethod

class Vehicle(ABC):           #abstract class

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

mycar = Car()
mycar.start()
mycar.stop()
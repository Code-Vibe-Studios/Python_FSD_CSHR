class Father:
    def vehicle(self):
        print("This is Father's car")

class Mother:
    def house(self):
        print("This is mother's house")

class Child(Father, Mother):
    pass

child = Child()
child.house()
child.vehicle()

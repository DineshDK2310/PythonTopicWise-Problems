class Bike:
    def __init__(self):
        print("Bike Is Ready")

    def brand(self):
        print("KTM")

    def MaxSpeed(self):
        print("250km")

    def cc(self):
        print("Engine CC:250cc")

class Duke(Bike):
    def __init__(self):
        super().__init__()
        print("Name:Duke")

    def brand(self):
        print("Brand:KTM")

    def MaxSpeed(self):
        print("MaxSpeed:250km")

    def color(self):
        print("Color:Orange and Black")

Vechicle = Duke()

Vechicle.brand()
Vechicle.MaxSpeed()
Vechicle.color()
Vechicle.cc()
class Bike:
    def __init__(self, owner , brand):
        self.owner = owner
        self.brand = brand

    def speed(self, speed):
        return "{} {}".format(self.brand, speed)


duke = Bike("Dinesh", "KTM")
print(duke.speed("Bike Maximum Speed is 250km"))
class Bike:
    type="Vehicle"

    def __init__(self,owner,brandName):
        self.owner=owner
        self.brandName=brandName

Duke=Bike("Dk","KTM")
Ns=Bike("Dk","BAJAJ")


print("Duke is a {}".format(Duke.__class__.type))
print("Ns is a {}".format(Duke.__class__.type))

print("Duke Bike Details:{},{}".format(Duke.owner,Duke.brandName))
print("NS Bike Details:{},{}".format(Ns.owner,Ns.brandName))


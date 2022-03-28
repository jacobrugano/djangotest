class Car:
    def __init__ (self,name,brand,price):
        self.name = name
        self.brand = brand
        self.price = price
    
    def getName(self):
        return self.name
    def getBrand(self):
        return self.brand
    def getPrice(self):
        return self.price
    def setName(self,newname):
        self.name = newname


newCar = Car("toyota vitz","toyota", 2000)
carcar = newCar.getName()
carcar2 = newCar.getBrand()
newCar.setName("Mercedez")
mycar = newCar.getName()
print (mycar)
print (carcar2)
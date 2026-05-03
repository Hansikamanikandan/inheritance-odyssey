class Vehicle:
    def getdetails(self):
        self.make = input("Enter Make: ")
        self.year = input("Enter Year: ")
        self.color = input("Enter Color: ")

    def display_info(self):
        print("\nMake:", self.make)
        print("Year:", self.year)
        print("Color:", self.color)


class Car(Vehicle):
    def getCarDetails(self):
        self.model = input("Enter Model: ")
        self.capacity = input("Enter Capacity: ")

    def Display_car(self):
        print("\nCar Model:", self.model)
        print("Capacity:", self.capacity)


class Bike(Vehicle):
    def getBikeDetails(self):
        self.type = input("Enter Bike Type: ")
        self.mileage = input("Enter Mileage: ")

    def Display_bike(self):
        print("\nBike Type:", self.type)
        print("Mileage:", self.mileage)


print("\n--- Car Details ---")
c = Car()
c.getdetails()
c.getCarDetails()
c.display_info()
c.Display_car()

print("\n--- Bike Details ---")
b = Bike()
b.getdetails()
b.getBikeDetails()
b.display_info()
b.Display_bike()

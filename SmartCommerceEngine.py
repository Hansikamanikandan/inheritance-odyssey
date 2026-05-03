class Product:
    def GetDetails(self):
        self.id = input("Enter Product ID: ")
        self.name = input("Enter Product Name: ")
        self.price = float(input("Enter Price: "))

    def add_to_cart(self):
        print("Product added to cart.")

    def display(self):
        print("\nID:", self.id)
        print("Name:", self.name)
        print("Price:", self.price)


class Electronics(Product):
    def GetElectronicsDetails(self):
        self.brand = input("Enter Brand: ")
        self.warranty = input("Enter Warranty: ")

    def Display(self):
        self.display()
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)


class Clothing(Product):
    def GetClothDetails(self):
        self.type = input("Enter Clothing Type: ")
        self.size = input("Enter Size: ")
        self.color = input("Enter Color: ")

    def Display(self):
        self.display()
        print("Type:", self.type)
        print("Size:", self.size)
        print("Color:", self.color)


print("\n--- Electronics ---")
e = Electronics()
e.GetDetails()
e.GetElectronicsDetails()
e.add_to_cart()
e.Display()

print("\n--- Clothing ---")
c = Clothing()
c.GetDetails()
c.GetClothDetails()
c.add_to_cart()
c.Display()

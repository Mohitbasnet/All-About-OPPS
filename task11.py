# Q-6: Ice-Cream Scoops and Bowl shop
# Create a class Scoop which has one public property flavor and one private proptery price. Take flavor values during object creation.

# Create a class Bowl with private prperty scoop_list which will have list of scoopd object.

# Create a method add_scoops in Bowl class which will add any no of Scoop objects given as parameter and store it in scoops_list.

# Make getter and setter method for price property.

# Make a method display to display flavour and price of each Scoop in scoop_list and print total price of the bowl by adding all flavour scoops prices.

# Make a method sold in both Scoop class and Bowl class to print no of quantity sold.
class Scoop:
    def __init__(self, flavor, price):
        self.flavor = flavor
        self.__price = price  # Private property

    def sold(self, quantity):
        print(f"{quantity} scoops of {self.flavor} sold.")

    # Getter and setter for price property
    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


class Bowl:
    def __init__(self):
        self.__scoop_list = []  # Private property

    def add_scoops(self, *scoops):
        for scoop in scoops:
            if isinstance(scoop, Scoop):
                self.__scoop_list.append(scoop)
            else:
                print("Invalid scoop object.")

    def display(self):
        total_price = 0
        for scoop in self.__scoop_list:
            print(f"Flavor: {scoop.flavor}, Price: ${scoop.get_price()}")
            total_price += scoop.get_price()
        print(f"Total Price: ${total_price}")

    def sold(self, quantity):
        print(f"{quantity} bowls sold.")


# Example usage:
scoop1 = Scoop("Chocolate", 2.5)
scoop2 = Scoop("Vanilla", 2.0)
scoop3 = Scoop("Strawberry", 3.0)

bowl = Bowl()
bowl.add_scoops(scoop1, scoop2, scoop3)

bowl.display()
scoop1.sold(5)
bowl.sold(10)

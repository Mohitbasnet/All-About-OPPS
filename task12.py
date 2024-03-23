# Q-7:Ice-Cream Bowl continue..
# Making advancement in the above classes. Scoop and Bowl

# Introduce a property max_scoops in Bowl class to signify maximum scoops that a bowl can have, exceeding that it will display Bowl is full. Take default value as 3.

# no_of_scoop in Scoop class with default value of 1

# Print <flavour> added with every scoop added.


class Scoop:
    def __init__(self, flavor, price, no_of_scoops=1):
        self.flavor = flavor
        self.__price = price  # Private property
        self.no_of_scoops = no_of_scoops

    def sold(self, quantity):
        print(f"{quantity} scoops of {self.flavor} sold.")

    # Getter and setter for price property
    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


class Bowl:
    def __init__(self, max_scoops=3):
        self.__scoop_list = []  # Private property
        self.max_scoops = max_scoops

    def add_scoops(self, *scoops):
        for scoop in scoops:
            if len(self.__scoop_list) >= self.max_scoops:
                print("Bowl is full.")
                break
            if isinstance(scoop, Scoop):
                self.__scoop_list.append(scoop)
                print(f"{scoop.flavor} added.")
            else:
                print("Invalid scoop object.")

    def display(self):
        total_price = 0
        for scoop in self.__scoop_list:
            print(f"Flavor: {scoop.flavor}, Price: ${scoop.get_price()}, No of Scoops: {scoop.no_of_scoops}")
            total_price += scoop.get_price() * scoop.no_of_scoops
        print(f"Total Price: ${total_price}")

    def sold(self, quantity):
        print(f"{quantity} bowls sold.")


# Example usage:
scoop1 = Scoop("Chocolate", 2.5, 2)
scoop2 = Scoop("Vanilla", 2.0)
scoop3 = Scoop("Strawberry", 3.0)

bowl = Bowl()
bowl.add_scoops(scoop1, scoop2, scoop3)
bowl.display()

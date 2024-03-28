# Constructor example 1

class Phone:
    def __init__(self, price, brand, camera):
        print('Inside phone constructor')
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('Buying a phone')


class SmartPhone(Phone):
    pass

s = SmartPhone(200,'apple',13)

s.buy()

# constructor example 2

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print ("Inside SmartPhone constructor")

s=SmartPhone("Android", 2)
# s.brand
class Atm:
    
    def __init__(self):
        self.pin = ""
        self.__balance= 0
        self.menu()

    def get_balance(self):
        return self.__balance

    def set_balance(self,new_value):
        if type(new_value) == int:
           self.__balance = new_value

        else:
            print("Kutai khanxas vai")
    def menu(self):
        user_input = input("""
                Hello, how would you like to proceed?
                1. Enter 1 to create pin
                2. Enetr 2 to deposit
                3. Enter 3 to withdraw
                4. Enter 4 to check balance
                5. Enter 5 to exit 
        """)
        if user_input=="1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("good luck")

    def create_pin(self):
        self.pin = input("Enter your pin")
        print("Pin set successfully")
    def deposit(self):
        temp = input ("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            self.__balance = self.__balance + amount
            print("Deposited successfully")
        else:
            print("Invalid pin")
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            if amount<self.__balance:
                self.__balance = self.__balance - amount
                print("Operation seccessful")
            else:
                print("Insufficient funds")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print(self.__balance)

        else:
            print("Invalid pin")



obj = Atm()
obj.get_balance()




# List of object

class Person:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender


p1 = Person("Mohit", "Male")
p3 = Person("Rohit", "Male")
p2 = Person("Sohit", "Male")

l = [p1,p2,p3]


for i in L:
    print(i.name,i.gender)

# Dict of objects
class Person:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender


p1 = Person("Mohit", "Male")
p3 = Person("Rohit", "Male")
p2 = Person("Sohit", "Male")

D = [p1,p2,p3]


for i in D:
    print(D[i].name)



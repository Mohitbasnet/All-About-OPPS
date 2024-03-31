# Abstraction example

# this is abstract class
from abc import ABC, abstractmethod
class BankApp(ABC):

    def database(self):
        print('Connectd to database')

    @abstractmethod
    def security(self):
        pass

    @abstractmethod
    def display(self):
        pass

class MobileApp(BankApp):

    def mobile_login(self):
        print('Login into mobile')
    
    def security(self):
        print("Mobile App security")
    
    def display(self):
        print("Mobile display")

    
s = MobileApp()
s.mobile_login()



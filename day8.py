
# Aggregation example
class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def print_address(self):
        print(self.address.get_city(),self.address.pin,self.address.state)

    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.edit_address(new_city,new_pin,new_state)


class Address:

    def __init__(self, city, pin, state):
        self.__city = city
        self.pin = pin
        self.state = state

    # To get the private varibale of Address class
    def get_city(self):
        return self.__city

    def edit_address(self, new_city, new_pin, new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state



add1 = Address('Kathmandu', '4470', 'Bagmati')
cust = Customer('Mohit','Male',add1)

cust.print_address()

cust.edit_profile('Rohit','KTM',1111,'Sudurpashcim')
cust.print_address()



# Inheritance example

# parent
class User:

  def __init__(self):
    self.name = 'Mohit'
    self.gender = 'male'

  def login(self):
    print('login')

# child
class Student(User):

#   def __init__(self):
#     self.rollno = 100

  def enroll(self):
    print('enroll into the course')


user = User()

student = Student()

# print(student.rollno)
print(student.name)
print(student.login())
student.enroll()
#Attribute example
class Person:
    def __init__(self,name,country):
        self.name = name
        self.country = country
    
    def greet(self):
        if self.country == "india":
            print("Namastey", self.name)

        else:
            print("Hello", self.name)



p = Person("Mohit","india")
p.greet()
print(p.country)


#Pass by Reference example
class Person1:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    
# Outside the class > funtion
def greet(person):
    print("Hi my name is",person.name, "and I am a",person.gender)
    p1 = Person1("Rohit","Other")
    return p1


p = Person1("Mohit","Male")
x = greet(p)
print(x.name)
print(x.gender)

# instance variable
class Person2:
    def __init__(self,name,country):
        self.name = name
        self.country = country

p1 = Person2('Mohit', "Nepal")
p2 = Person2("Rohit", "Japan")
print(p1)
print(p2)
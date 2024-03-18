# Q1:Count number of instances of a class created in Python?
# Example: Say Car is any class.

# maruti = Car()
# bmw = Car()
# honda = Car()
# So after creating above instances. We want to count how many instances are created of Car class.

# For above example no of instances = 3.

# Write a program for above problem.

class Car:
    count = 0
    def __init__(self):
        Car.count +=1


maruti = Car()
bmw = Car()
honda = Car()


print("Number of instance are:",Car.count)
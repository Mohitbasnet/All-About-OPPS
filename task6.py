class Car:
    count = 0
    def __init__(self):
        Car.count +=1


maruti = Car()
bmw = Car()
honda = Car()


print("Number of instance are:",Car.count)
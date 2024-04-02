# Problem-2: Class Inheritence
# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

# Use the following code for your parent Vehicle class.

class Vehicle:
    def seating_capacity(self, capacity=50):
        return f'This vehicle has a seating capacity of {capacity} passengers.'

class Bus(Vehicle):
    pass

# Example usage
bus = Bus()
print(bus.seating_capacity())  # Output: This vehicle has a seating capacity of 50 passengers.



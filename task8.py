# Q-3: Find the area of a rectangle.
# Approach:

# The class name should be Rectangle.
# The constructor should accept two parameters length and height but you can't pass the values directly to it while creating the constructor. E.g., rectangle = Rectangle(length=10, height=8) <-- you can't do that while creating the instances.
# Create a method called area() which has no parameters.
# Create a method called is_square() which also has no parameters. Return True if the rectangle is a square otherwise return False.
# If you are using a if-else block inside the is_square() method, then use the one-linear syntax.


class Rectangle:
    def __init__(self, *args):
        if len(args) == 2:
            self.length = args[0]
            self.height = args[1]
        else:
            raise ValueError("Length and height must be provided.")

    def area(self):
        return self.length * self.height

    def is_square(self):
        return True if self.length == self.height else False


rectangle = Rectangle(10, 8)
print(rectangle.area())  
print(rectangle.is_square())  

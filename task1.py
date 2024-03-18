# Q-1: Rectangle Class
# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.

# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.

# Eg. After making above classes and methods, on executing below code:-

# my_rectangle = Rectangle(3 , 4)
# my_rectangle.display()
# Output:

# The length of rectangle is:  3
# The width of rectangle is:  4
# The perimeter of rectangle is:  14
# The area of rectangle is:  12


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print("The length of rectangle is:", self.length)
        print("The width of rectangle is:", self.width)
        print("The perimeter of rectangle is:", self.perimeter())
        print("The area of rectangle is:", self.area())

# Testing the Rectangle class
my_rectangle = Rectangle(3, 4)
my_rectangle.display()

#`Problem-4:` Write a program that has an abstract class Polygon. 
# Derive two classes Rectangle and Triamgle from Polygon and write methods to get the details of their dimensions and hence calculate the area.

from abc import ABC, abstractmethod

class Polygon(ABC):
    def __init__(self, sides):
        self.sides = sides
    
    @abstractmethod
    def area(self):
        pass
    
    def get_dimensions(self):
        return self.sides

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width])
    
    def area(self):
        length, width = self.get_dimensions()
        return length * width

class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__([base, height])
    
    def area(self):
        base, height = self.get_dimensions()
        return 0.5 * base * height

# Example usage:
if __name__ == "__main__":
    rectangle = Rectangle(5, 4)
    triangle = Triangle(3, 6)
    
    print("Rectangle Area:", rectangle.area())
    print("Triangle Area:", triangle.area())

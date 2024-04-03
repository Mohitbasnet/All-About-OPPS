# Problem-3: Write a program that has a class Point. 
# Define another class Location which has two objects (Location & Destination) of class Point.
#  Also define a function in Location that prints the reflection of Destination on the x axis.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Location(Point):
    def __init__(self, location_x, location_y, destination_x, destination_y):
        super().__init__(location_x, location_y)
        self.destination = Point(destination_x, destination_y)
    
    def print_reflection_on_x_axis(self):
        reflected_y = -self.destination.y
        reflected_destination = Point(self.destination.x, reflected_y)
        print("Reflection of Destination on the x axis:", reflected_destination.x, reflected_destination.y)

# Example usage
location = Location(3, 4, 7, 9)
location.print_reflection_on_x_axis()

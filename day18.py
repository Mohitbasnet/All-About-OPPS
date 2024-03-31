# Example of Method overloading
# This concept comes bcoz the code will be more clean in reading.
# But we cannot implement this in python.
class Shape: 
    def area(self, radius):
        return 3.14*radius*radius

    def area(self,l,b):
        return l*b


obj1 = Shape()
print(obj1.area(5,3))

# By this way we can implement the method overloading if you want to
# THis is smart way
class Shape:

  def area(self,a,b=0):
    if b == 0:
      return 3.14*a*a
    else:
      return a*b

s = Shape()

print(s.area(2))
print(s.area(3,4))
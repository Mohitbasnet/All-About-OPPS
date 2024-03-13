class Point:
    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y
    def __str__(self):
        return '<{},{}>'.format(self.x_cod ,self.y_cod)

    def euclidean_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5

    def distance_from_origin(self):
        #return (self.x_cod**2 + self.y_cod**2)**0.5
        #Here object class ko vitra banaiyeko xa
        return self.euclidean_distance(Point(0,0))



class Line:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

    
    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A,self.B,self.C)
    

    def point_on_line(line,point):

        if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:
            return "Lies on line"
        else:
            return "Does not lie on the line"

    def shortest_distance(line,point):
        return abs(line.A*point.x_cod + line.B*point.y_cod + line.C)/(line.A**2 + line.B**2)**0.5

    def intersect(line1,line2):
        denominator = line1.A * line2.B - line2.A * line1.B

        # Handle cases where lines are parallel or intersecting
        if denominator == 0:
            if line1.A== line2.A and line.B== line2.B:
            
                 print("Lines are intersecting.")
                 return False
            else:
            # Lines are parallel (never intersect)
                print("Lines are parallel.")
                return False

        x = abs(line1.B*line2.C-line2.B*line1.C)/(line1.A*line2.B - line2.A*line1.B)
        y = abs(line2.A*line1.C-line1.A*line2.C)/(line1.A*line2.B - line2.A*line1.B)
        print("Lines intersect at point (", x, ",", y, ").")
        return True

p2 = Point(10,10)
# print(p1.euclidean_distance(p2))
print(p2.distance_from_origin())
#objects of line
l1 = Line(2,-3,0)
l2 = Line(2,-1,4)
p1 = Point(1,10)
print(l1)
print(p1)
print(l1.point_on_line(p1))
print(l1.shortest_distance(p1))

print(l1.intersect(l2))
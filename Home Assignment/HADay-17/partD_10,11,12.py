# Part D: Hierarchical Inheritance
# 10.Create a parent class Shape:
# oAttribute: name
# oMethod: area() returns Not implemented
# 11.Create child classes:
# oRectangle: Inherit from Shape, implement area().
# oCircle: Inherit from Shape, implement area() using math.pi.
# oTriangle: Inherit from Shape, implement area() as 0.5 * base * height.
# 12.Test instances of Rectangle, Circle, and Triangle.

import math
class Shape:
    def __init__(self , name):
        self.name = name
    def area(self):
        return"Not Implemented"
class Rectangle(Shape):
    def __init__(self , name , length , width):
        self.name = name
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
class Triangle(Shape):
    def __init__(self , name , base , height):
        super().__init__(name)
        self.base = base 
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
rectangle = Rectangle("Rectangle", 4, 5)
circle = Circle("Circle", 3)
triangle = Triangle("Triangle", 6, 8)

shapes = [rectangle, circle, triangle]

for shape in shapes:
    print(f"Name: {shape.name}, Area: {shape.area():.2f}")

    




# Part B: Abstraction with Abstract Classes
# 4.Create an abstract class Shape:
# oAbstract method: area()
# oAbstract method: perimeter()
# 5.Create concrete subclasses:
# oRectangle: Implement area() and perimeter().
# oCircle: Implement area() and perimeter().
# 6.Test by creating instances of Rectangle and Circle and calling their methods.
from abc import ABC , abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
         return 2 * (self.length + self.width)
class Circle(Rectangle):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2) #use 3.14 value either import math & use math.pi
    def perimeter(self):
        return 2 * math.pi * self.radius
rectangle = Rectangle(4,5)
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimmeter: {rectangle.perimeter()}")

circle = Circle(5)
print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")


        

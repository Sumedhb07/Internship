# Create a Rectangle Class
# Attributes: length, width.
# Methods:
# area() — Returns the area of the rectangle.
# perimeter() — Returns the perimeter.
# Test it: Create a few instances and print their area and perimeter.
class Rectangle:
    def  __init__(self , length , width):
        self.length = length
        self.width = width
    def area(self):
        self.area = self.length * self.width
        print(self.area)
    
    def perimeter(self):
        self.perimeter = 2 * (self.length + self.width)
        print(self.perimeter)

    # def Result(self):
    #      self.area()
    #      self.perimeter()
        print("The Area of Rectangle: ",self.area)
        print("The Perimeter of Rectangle",self.perimeter)

obj = Rectangle(5,5)   
obj.area ()
obj.perimeter ()

  
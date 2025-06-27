# Rectangle Class
# Private Attributes: __width and __height.

# Properties:

# width and height with getters and setters (no negatives).

# Method:

# area() returns the area of the rectangle.
class Rectangle:
    def __init__(self):
        self.__width = 0
        self.__height  = 0
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self , value):
        
        


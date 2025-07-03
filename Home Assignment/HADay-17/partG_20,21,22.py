#  Part G: Complex Challenges
# 20.Shape Manager:
# oCreate a parent class Shape with a method draw().
# oCreate child classes Square, Rectangle, Circle, and implement their draw() method.
# oMaintain a list of shapes and iterate over them, calling draw().
class Shape:
    def draw(self):
        pass
class Square:
    def __init__(self,side):
        self.side = side
    def draw(self):
        print(f"Drawing a square with side {self.side}")
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing a Rectangle with width {self.width} and height {self.height}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Drawing a Circle with radius {self.radius}")

# Shape Manager
class ShapeManager:
    def __init__(self):
        self.shapes = []
    def add_shape(self, shape):
        self.shapes.append(shape)

    def draw_shapes(self):
        for shape in self.shapes:
            shape.draw()

# Test the Shape Manager
shape_manager = ShapeManager()

shape_manager.add_shape(Square(4))
shape_manager.add_shape(Rectangle(3, 5))
shape_manager.add_shape(Circle(2))

shape_manager.draw_shapes()



# 21.Employee Hierarchy Simulation:
# oCreate parent class Person (name, age).
# oCreate child classes:
# Employee inherits Person (add salary).
# Teacher inherits Employee (add subject).
# Engineer inherits Employee (add specialization).
# oImplement a display() method in each class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display(self):
        super().display()
        print(f"Salary: ${self.salary:.2f}")

class Teacher(Employee):
    def __init__(self, name, age, salary, subject):
        super().__init__(name, age, salary)
        self.subject = subject

    def display(self):
        super().display()
        print(f"Subject: {self.subject}")

class Engineer(Employee):
    def __init__(self, name, age, salary, specialization):
        super().__init__(name, age, salary)
        self.specialization = specialization

def display(self):
        super().display()
        print(f"Specialization: {self.specialization}")

# Test the classes
person = Person("John Doe", 30)
employee = Employee("Jane Smith", 35, 50000)
teacher = Teacher("Bob Johnson", 40, 60000, "Mathematics")
engineer = Engineer("Alice Williams", 32, 70000, "Software Development")

print("Person Details:")
person.display()

print("\nEmployee Details:")
employee.display()

print("\nTeacher Details:")
teacher.display()

print("\nEngineer Details:")
engineer.display()


# 22.Geometric Calculator:
# oCreate parent class Polygon (attribute sides).
# oCreate child classes:
# Square: area = side^2.
# Rectangle: area = length * breadth.
# Triangle: area = (base * height)/2.
# oPolymorphically call area methods.
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def area(self):
        pass  # Base class method

class Square(Polygon):
    def __init__(self, side):
        super().__init__(4)
        self.side = side

    def area(self):
        return self.side ** 2

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        super().__init__(4)
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__(3)
        self.base = base
        self.height = height
def area(self):
        return (self.base * self.height) / 2

# Geometric Calculator
def calculate_area(polygon):
    print(f"Area of {type(polygon).__name__}: {polygon.area()}")

# Test the Geometric Calculator
square = Square(4)
rectangle = Rectangle(3, 5)
triangle = Triangle(6, 8)

calculate_area(square)
calculate_area(rectangle)
calculate_area(triangle)



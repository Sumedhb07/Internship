# 🐍 DAY 17 – HOME ASSIGNMENTS: Inheritance & Polymorphism
# (Single, Multiple, Multilevel, Hierarchical Inheritance, Polymorphism, Method Overriding & Super Usage.)
# Part A: Single Inheritance
# 1.Create a parent class Person with attributes:
#name, age.
#Method: display().
class person:
    def __init__(self , name ,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
person1 = person("Sumedh",18)
person1.display()

# 2.Create a child class Student that inherits Person:
# oAdd roll_number attribute.
# oOverride the display() method.
class Person:
    def __init__(self , name , age ):
      self.name = name 
      self.age = age
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
class Student(Person):
    def __init__(self , name , age , roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll Number: {self.roll_number}")
person = Person("Prasad" , 19)
student = Student("Sumedh" , 18 , 55)

print("Person Details: ")
person.display()

print("Student Details: ")
student.display()
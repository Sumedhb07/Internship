#  Part B: Advanced Attribute Handling
# 3.Instance vs. Class Attribute Demo
# oCreate a class Student:
# Class Attribute: school_name = "ABC High School"
# Instance Attributes: name, age, marks
# Method:
# display() – Shows student details and the school name.
# oChange school_name for one object, and observe the result on other instances.
class Student:
    school_name = "ABC High School"
    def __init__(self , name , age , marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
student1 = Student("Sumedh" , 18 , 95)
student2 = Student("Prasad" , 19 , 96)
    
print("initial Details")
student1.display()
print()
student2.display()

Student.school_name = "XYZ High school"
print("Upadated Details")
student1.display()
print()
student2.display()
student1.school_name = "BMW High school"
print("Upadated Details")
student1.display()
print()   
student2.display()




# 4.Employee Salary Manager
# oCreate an Employee class:
# Attributes:
# Instance: name, salary.
# Class Attribute: min_wage = 10000.
# Method:
# adjust_salary() – If salary < min_wage, set it to min_wage.
# display() – Shows employee name and salary.
# oTest with different employee instances.
class Employee:
    min_wage = 10000
def __init__(self , name , salary):
    self.name = name
    self.salary = salary
    self.adjust_salary()
def adjust_salary(self):
     if self.salary < Employee.min_wage:
        self.salary = Employee.min_wage
        print(f"Adjusted {self.name}'s salary to meet the minimum wage.")

def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")

# Test with different employee instances
employee1 = Employee("prasad", 12000)
employee2 = Employee("aditya", 8000)
employee3 = Employee("Sumedh", 15000)

# Display employee details
print("\nEmployee Details:")
employee1.display()
print()
employee2.display()
print()
employee3.display()




    
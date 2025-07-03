# Part G: Bonus Challenges for Day 18
# 14.Create an abstract class PaymentMethod:
# oAbstract method: pay(amount)
# oSubclasses:
# CreditCard
# PayPal
# BankTransfer
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def __init__(self, card_number, expiration_date, cvv):
        self.__card_number = card_number
        self.__expiration_date = expiration_date
        self.__cvv = cvv

    def pay(self, amount):
        print(f"Paying {amount} using credit/debit card {self.__card_number[-4:]}")
        return f"Payment of {amount} successful."

class PayPal(PaymentMethod):
    def __init__(self, email):
        self.__email = email

    def pay(self, amount):
        print(f"Paying {amount}rs using PayPal account {self.__email}")
        return f"Payment of {amount}rs successful."

class BankTransfer(PaymentMethod):
    def __init__(self, account_number):
        self.__account_number = account_number

    def pay(self, amount):
        print(f"Paying {amount}rs using bank transfer to account {self.__account_number[-4:]}")
        return f"Payment of {amount}rs successful."

# Test instances
credit_card = CreditCard("1234567890123456", "12/2025", "123")
print(credit_card.pay(100))

paypal = PayPal("user@example.com")
print(paypal.pay(50))

bank_transfer = BankTransfer("1234567890")
print(bank_transfer.pay(200))


# 15.Create an abstract class Notification:
# oAbstract method: send_message()
# oSubclasses:
# EmailNotification
# SMSNotification
# PushNotification
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send_message(self, message):
        pass

class EmailNotification(Notification):
    def __init__(self, email):
        self.__email = email

    def send_message(self, message):
        print(f"Sending email to {self.__email}: {message}")
        return f"Email sent to {self.__email}."

class SMSNotification(Notification):
    def __init__(self, phone_number):
        self.__phone_number = phone_number

    def send_message(self, message):
        print(f"Sending SMS to {self.__phone_number}: {message}")
        return f"SMS sent to {self.__phone_number}."

class PushNotification(Notification):
    def __init__(self, device_id):
        self.__device_id = device_id

    def send_message(self, message):
        print(f"Sending push notification to device {self.__device_id}: {message}")
        return f"Push notification sent to device {self.__device_id}."

# Test instances
email_notification = EmailNotification("user@example.com")
print(email_notification.send_message("Hello, this is an email notification."))

sms_notification = SMSNotification("+1234567890")
print(sms_notification.send_message("Hello, this is an SMS notification."))

push_notification = PushNotification("device123")
print(push_notification.send_message("Hello, this is a push notification."))


# 16.Build a robust Student Registration System:
# oAbstract class: Person
# Abstract method: get_role()
# oSubclasses:
# Student (encapsulates marks and validates range).
# Teacher (encapsulates salary).
# AdminStaff (encapsulates department).

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    @abstractmethod
    def get_role(self):
        pass

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.__marks = self.__validate_marks(marks)

    def __validate_marks(self, marks):
        if 0 <= marks <= 100:
            return marks
        else:
            raise ValueError("Invalid marks. Marks should be between 0 and 100.")

    def get_marks(self):
        return self.__marks

    def get_role(self):
        return "Student"

class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def get_role(self):
        return "Teacher"

class AdminStaff(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.__department = department

    def get_department(self):
        return self.__department

    def get_role(self):
        return "Admin Staff"

# Test instances
student = Student("Sumedh", 20, 95)
print(f"Name: {student.get_name()}, Age: {student.get_age()}, Role: {student.get_role()}, Marks: {student.get_marks()}")

teacher = Teacher("prasad", 35, 60000)
print(f"Name: {teacher.get_name()}, Age: {teacher.get_age()}, Role: {teacher.get_role()}, Salary: ${teacher.get_salary():.2f}")

admin_staff = AdminStaff("piyush", 40, "HR")
print(f"Name: {admin_staff.get_name()}, Age: {admin_staff.get_age()}, Role: {admin_staff.get_role()}, Department: {admin_staff.get_department()}")

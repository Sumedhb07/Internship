# Create a Car Class
# Attributes:
# brand (string), model (string), speed (initially 0).
# Methods:
# accelerate() — Increases speed by 10.
# brake() — Decreases speed by 5.
# display_speed() — Shows the current speed.
# Test it: Create a car object, call accelerate() and brake() a few times, and display the speed.
class car:
    def __init__(self , brand , model):
        self.brand = brand 
        self.model = model
        self.speed = 0
    def acceleration(self):
        self.speed += 10
    def brake(self):
        self.speed -= 5
    def display_speed(self):
        print(f"The current speed is:- {self.speed}")

c = car("BMW" , "M4")
c.acceleration()
c.brake()
c.display_speed()

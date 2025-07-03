# Part B: Multiple Inheritance
# 3.Create a class Engine:
# oMethod: start() returns Engine started.
# 4.Create a class MusicSystem:
# oMethod: play() returns Playing music.
# 5.Create a class Car that inherits from both Engine and MusicSystem:
# oMethod: drive() returns Car is driving.
# oTest by creating an object of Car and invoking methods from both parent classes.
class Engine:
    def start(self):
        return "Engine Started"
class MusicSystem:
    def play(self):
        return"Playing Music"
class Car(Engine , MusicSystem):
    def drive(self):
        return "Car is Driving"
car = Car()
print(car.start())
print(car.play())
print(car.drive())

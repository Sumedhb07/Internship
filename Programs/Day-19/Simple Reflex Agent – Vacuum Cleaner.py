# Simple Reflex Agent – Vacuum Cleaner
# 🔹Objective:
# Simulate a simple reflex agent for a 1D or 2D vacuum cleaner world.

# 🔹Instructions:
# Create an environment as a list of rooms: e.g. ['Dirty', 'Clean', 'Dirty']

# Agent starts at position 0.

# If the current position is 'Dirty' → clean it.

# Move to the next room and repeat.

# Stop when all rooms are clean.
class vacuum_cleaner:
    def __init__(self , envirnment):
        self.envirnment = envirnment 
        self.position = 0

    def clean(self):
        while dirty in self.envirnment:
            if dirty.envirnment[self.position] == "dirty":
                print("Cleaning room: ",self.position)
                print(f"Room {self.position} is clean")

    def move_room(self):
        
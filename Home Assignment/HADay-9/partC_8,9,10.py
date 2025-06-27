# Part C: Real-World Dictionary Use Cases
# 8.Contact Book
# oCreate a dictionary contacts with 3 people’s names as keys and their phone numbers as values.
# oAdd a new contact.
# oUpdate one contact’s number.
# oDelete one contact.
contacts = {"john": "123 456 7890","Alice": "987 654 3210","Bob": "555 222 7890"}
print("Initial Contacts:")
for name, number in contacts.items():
    print(f"{name}: {number}")

new_name = "Charlie"
new_number = "565 789 3578"
contacts[new_name] = new_number

print("\nContacts after adding new contact: ")
for name, number in contacts.items():
    print(f"{name}: {number}")

updated_name = "john"
updated_number = "111 222 5555"
contacts[updated_name] = updated_number
print("\n Contacts after updating contact:")
for name, number in contacts.items():
    print(f"{name}: {number}")

deleted_name = "Bob"
del contacts[deleted_name]
print("\nFinal Contacts:")
for name, number in contacts.items():
    print(f"{name}: {number}")



# 9.Inventory System
# oCreate a dictionary inventory where keys are product names ("pen", "notebook", "eraser") and values are quantities.
# oWrite a function update_stock(item, quantity) to increase stock.
# oIf item is not in inventory, add it.
# Initialize the inventory dictionary
inventory = {"pen": 10, "notebook": 5,"eraser": 8}

# Function to update stock
def update_stock(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"Updated inventory: {inventory}")

# Example usage
update_stock("pen", 3)        # Increases quantity of pens
update_stock("marker", 4)     # Adds marker as a new item


# 10.Student Marks
# Create a dictionary marks with subjects as keys and marks out of 100 as values.
# Calculate total marks and average.
# Print a message based on average:
# o>90: Excellent
# o70–90: Good
# o<70: Needs Improvement
# Create the dictionary with subject marks
marks = {
    "Math": 95,
    "Science": 88,
    "English": 92,
    "History": 76,
    "Art": 85}
# Calculate total and average
total_marks = sum(marks.values())
average_marks = total_marks / len(marks)

if average_marks > 90:
    message = "Excellent"
elif 70 <= average_marks <= 90:
    message = "Good"
else:
    message = "Needs Improvement"

print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Performance: {message}")



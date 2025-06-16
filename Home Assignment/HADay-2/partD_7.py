#7.Ask the user to enter their name and age print how many years are left until theyturn 100
name = input("Enter a Name:- ")
age = int(input("Enter a Age:- "))
calculation = 100 - age
print("\nName: ",name)
print("Age: ",age)
print(f"Hello {name}!")
print(f"You will turn 100 years old in {calculation} years")
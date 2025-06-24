#print the multiplication table of a number(user input)
num = int(input("Enter a number for print Table:- "))
print(f"Multiplication table of {num}")
for i in range(1,11):
    print(f"{num} * {i} = {num * i}")
    


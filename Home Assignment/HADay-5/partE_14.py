#14. Create a multiplication table from 1 to 5, like:
#1 x 1 = 1
#1 x 2 = 2
#...
#5 x 10 = 50
#num = int(input("Enter a number for print Table:- "))
#print(f"Multiplication table of {num}")
for i in range(1,6):
    for j in range(1,11):
        print(f"{i} * {j} = {i * j}")
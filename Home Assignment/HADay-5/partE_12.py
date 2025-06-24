# 12.Print a square pattern using nested for loops:
# * * * *
# * * * *
# * * * *
# * * * *
num = int(input("Enter the size  of the square:- "))
for i in range(num):
    for j in range(num):
        print('*', end=' ')
    print()
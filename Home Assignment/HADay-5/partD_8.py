# Part D: Patterns with Loops
# 8.Print the following right-angle triangle pattern using a for loop:
#    *
#   ***
#  *****
# *******
# Take a number n as input and print a triangle with n rows using *.
num=int(input("Enter a number: "))
for i in range(1,num+1):
    stars = '*' * (2 * i - 1)
    spaces = ' ' * (num - i)
    print(spaces + stars)
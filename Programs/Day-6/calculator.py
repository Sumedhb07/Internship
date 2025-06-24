#Calculator
def menu(arith,a,b):
    if arith == '+':
        print(a+b)
    elif arith == '-':
        print(a-b)
    elif arith == '*':
        print(a*b)
    else:
        print(a/b)
st=input("Enter the Operator to perform Operation(+,-,*,/) :- ")
p=int(input(" Enter First Number: " ))
q=int(input(" Enter Second Number: "))
menu(st,p,q)
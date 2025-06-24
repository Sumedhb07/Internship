data = [10,20,30,40]
try:
    index = int(input("Enter a index:- "))
    value = data[index]
    float_val = float(value)
    print(f"the float value at {index} is : {float_val} ")
except(IndexError,ValueError) as e:
    print("Index is out of Range /",e)
    print("Value cannot be converted to float /",e) 
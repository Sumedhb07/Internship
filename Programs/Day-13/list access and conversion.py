# Task 3: List Access and Conversion
# Instructions:
# Create a list: data = [10, 20, 30]
# Ask the user for an index.
# Access that index and convert it to a float.
# Catch both IndexError and ValueError.
no =10
list1 = []
for i in range(1,no+1):
    list1.append(int(input(f"Enter {i} no : ")))
    

try : 
    index_no = int(input(" Enter the index to be convert : "))
    A = float(list1[index_no])
    print(A)
except (IndexError,ValueError) as e:
    # print("Index not found ... ")
    # print("Invalid input .. ")
    print(e)
     
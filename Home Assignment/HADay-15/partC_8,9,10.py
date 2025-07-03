# Part C: Adding, Modifying, and Removing Columns
# 8.Add a New Column
# oAdd a column Pass which is True if Marks >= 40 else False.
import pandas as pd

# Create a dictionary with data
data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,18,19,18] , 
    'Marks' : [95,89,96,98,90]
}
# Create a DataFrame
students = pd.DataFrame(data)
students['pass'] = students['Marks'] <= 40
print("Updated DataFrame: ")
print(students)

# 9.Modify an Existing Column
# Increase every student’s marks by 5.
import pandas as pd

# Create a dictionary with data
data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,18,19,18] , 
    'Marks' : [95,89,96,98,90]
}
# Create a DataFrame
students = pd.DataFrame(data)

# Increase every student's marks by 5
students['Marks'] += 5

print("Updated DataFrame:")
print(students)


# 10.Remove a Column
# oDrop the Age column and print the resulting DF. 
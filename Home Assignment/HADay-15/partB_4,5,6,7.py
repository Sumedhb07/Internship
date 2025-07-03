# Part B: Selecting and Indexing
# 4.Column Selection
# From the students DF(DataFrame), select the Name column and print it.
import pandas as pd

# Create a dictionary with data
data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,18,19,18] , 
    'Marks' : [95,89,96,98,90]
} 

# Create a DataFrame
students = pd.DataFrame(data)

# Select the 'Name' column
names = students['Name']

print("Name Column:")
print(names)


# 5.Row Selection by Position
# oUse .iloc to print the first 3 rows.
import pandas as pd

# Create a dictionary with data
data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,18,19,18] , 
    'Marks' : [95,89,96,98,90]
}

# Create a DataFrame
students = pd.DataFrame(data)
first_three_rows = students.iloc[:3]
print("First 3 Rows: ")
print(first_three_rows)

# 6.Row Selection by Label
# Set Name as the index and use .loc to fetch a student by name.
import pandas as pd

# Create a dictionary with data
data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,18,19,18] , 
    'Marks' : [95,89,96,98,90]
}

# Create a DataFrame
students = pd.DataFrame(data)

# Set 'Name' as the index
students.set_index('Name', inplace=True)

# Select a student by name using .loc
student = students.loc['Prasad']

print("Student 'Prasad':")
print(student)


# 7.Conditional Selection
# Select students with Marks > 75.
# Select students with Age <= 20.
import pandas as pd

# Create a dictionary with data
data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,18,19,18] , 
    'Marks' : [95,89,96,98,90]
}

# Create a DataFrame
students = pd.DataFrame(data)
high_marks = students[students['Marks'] > 75]
high_Age = students[students['Age'] <= 20]
print(students)
print("Students with Marks with Greater than 75: ")
print(high_marks)
print("Students with Age Greater than Equal to 20: ")
print(high_Age)
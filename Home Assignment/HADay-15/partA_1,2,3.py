# 🐼 DAY 15 – HOME ASSIGNMENTS: Introduction to Pandas
#  Part A: Creating and Inspecting Series/DataFrames
# 1.Create a Series
# oCreate a Pandas Series from a list of 5 city names.
import pandas as pd

# Create a list of 5 city names
city_names = ['Nashik', 'Mumbai', 'pune', 'manmad', 'jalgaon']

# Create a Pandas Series from the list
city_series = pd.Series(city_names)

print("City Series:")
print(city_series)

# 2.Create a DataFrame
# oCreate a DataFrame called students with columns:
# Name (string), Age (int), Marks (float)
import pandas as pd

data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,18,19,18] , 
    'Marks' : [95,89,96,98,90]
} 
students = pd.DataFrame(data)
print("Students DataFrames: ")
print(students)

# 3.Check Properties
# oPrint:
# .shape
# .columns
# .dtypes
# .info()
# .describe() (for numeric columns)
import pandas as pd

# Create a dictionary with data
data = {
    'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,18,19,18] , 
    'Marks' : [95,89,96,98,90]
}

# Create a DataFrame
students = pd.DataFrame(data)

# Print properties
print("Shape:")
print(students.shape)
print("\nColumns:")
print(students.columns)
print("\nData Types:")
print(students.dtypes)
print("\nInfo:")
print(students.info())
print("\nDescription:")
print(students[['Age', 'Marks']].describe())


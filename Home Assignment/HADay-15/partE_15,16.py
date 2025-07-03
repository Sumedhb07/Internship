#  Part E: Aggregation and Grouping
# 15.Summary Stats
# Find the total, average, max, and min marks from the DF(DataFrame).
import pandas as pd

# Create a dictionary with data
data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,18,19,18] , 
    'Marks' : [95,89,96,98,90]
}
# Create a DataFrame
students = pd.DataFrame(data)
# Calculate summary statistics
total_marks = students['Marks'].sum()
average_marks = students['Marks'].mean()
max_marks = students['Marks'].max()
min_marks = students['Marks'].min()

print("Summary.....")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Max Marks: {max_marks}")
print(f"Min Marks: {min_marks}")


# 16.Grouping
# oAdd a column Class (e.g., Class A or Class B).
# oGroup the DF by Class and compute the average marks per class.
import pandas as pd

# Create a dictionary with data
data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,18,19,18] ,
    'Class': ['A', 'A', 'A', 'B', 'B', 'B', 'B'],
    'Marks' : [95,89,96,98,90]
}
# Create a DataFrame
students = pd.DataFrame(data)
#Group the DF by Class and compute the average marks per class
average_marks_per_class = students.groupby('Class')['Marks'].mean()

print("Average Marks per Class:")
print(average_marks_per_class)




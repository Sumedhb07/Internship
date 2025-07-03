# Part F: Miscellaneous Practice
# 17.Sorting
# oSort the DF by Marks in ascending and then in descending order.
import pandas as pd

# Create a dictionary with data
data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,18,19,18] , 
    'Marks' : [95,89,96,98,90]
}
# Create a DataFrame
students = pd.DataFrame(data)
# Sort the DF by Marks in ascending order
ascending_order = students.sort_values(by='Marks', ascending=True)

# Sort the DF by Marks in descending order
descending_order = students.sort_values(by='Marks', ascending=False)

print("Ascending Order:")
print(ascending_order)
print("\nDescending Order:")
print(descending_order)



# 18.Rename Columns
# oRename columns Name -> Student Name, Marks -> Total Marks.
# Rename columns
import pandas as pd

# Create a dictionary with data
data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,18,19,18] , 
    'Marks' : [95,89,96,98,90]
}
# Create a DataFrame
students = pd.DataFrame(data)
students = students.rename(columns={'Name': 'Student Name', 'Marks': 'Total Marks'})

print("Updated DataFrame:")
print(students)



# 19.Export DF(DataFrame)
# oExport the final DF to a .csv file named student_records.csv.
import pandas as pd

# Create a dictionary with data
data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,18,19,18] , 
    'Marks' : [95,89,96,98,90]
}
# Create a DataFrame
students = pd.DataFrame(data)
#Export the DF to a .csv file
students.to_csv('student_records.csv', index=False)

print("DataFrame exported to student_records.csv")



# 20.Apply a Function
# oUse .apply() to categorize marks:
# Marks >= 80: Excellent
# Marks >= 60: Good
# Marks >= 40: Pass
# Marks < 40: Fail
import pandas as pd

# Create a dictionary with data
data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,18,19,18] , 
    'Marks' : [95,89,96,98,90]
}
# Create a DataFrame
students = pd.DataFrame(data)
# Define a function to categorize marks
def categorize_marks(marks):
    if marks >= 80:
        return 'Excellent'
    elif marks >= 60:
        return 'Good'
    elif marks >= 40:
        return 'Pass'
    else:
        return 'Fail'

# Apply the function to the 'Total Marks' column
students['Grade'] = students['Total Marks'].apply(categorize_marks)

print("Updated DataFrame:")
print(students)

# 21.Check Duplicates
# oIdentify and remove duplicate rows in the DF.
# Identify duplicate rows
import pandas as pd

# Create a dictionary with data
data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,18,19,18] , 
    'Marks' : [95,89,96,98,90]
}
# Create a DataFrame
students = pd.DataFrame(data)
duplicates = students.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# Remove duplicate rows
students = students.drop_duplicates()

print("\nUpdated DataFrame:")
print(students)




# 22.Merge Two DataFrames
# oCreate another DF with columns Name and Class Teacher.
# oMerge both DFs on the Name column.
import pandas as pd

# Create a dictionary with data
data1 = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,18,19,18] , 
    'Marks' : [95,89,96,98,90]
}
# Create a DataFrame
students = pd.DataFrame(data1)
data2 = {
    'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Class Teacher': ['Mr. Badgujar', 'Mr. Patil' , 'Mr. pawar', 'Mr. sangle', 'Mr. Aher']
}
teachers = pd.DataFrame(data2)
# Merge both DataFrames on the Name column
merged_df = pd.merge(students, teachers, on='Name')

print("Merged DataFrame:")
print(merged_df)





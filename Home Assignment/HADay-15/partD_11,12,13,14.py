# Part D: Handling Missing Values
# 11.Introduce Missing Values
# oCreate a DF(DataFrame) with columns Name, Age, Marks where some Age and Marks values are NaN.
import pandas as pd
import numpy as np
# Create a dictionary with data
data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,np.nan,19,np.nan] , 
    'Marks' : [95,89,np.nan,98,90]
}
# Create a DataFrame
students = pd.DataFrame(data)
print("DataFrame with Missing values: ")
print(students)


# 12.Check for Missing Values
# oUse .isnull() and .sum() to count NaNs.
import pandas as pd
import numpy as np
# Create a dictionary with data
data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,np.nan,19,np.nan] , 
    'Marks' : [95,89,np.nan,98,90]
}
# Create a DataFrame
students = pd.DataFrame(data)
missing_values = students.isnull().sum()

print("missing values count: ")
print(missing_values)

# 13.Fill Missing Values
# oFill NaN in the Marks column with the average marks.
import pandas as pd
import numpy as np
# Create a dictionary with data
data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,np.nan,19,np.nan] , 
    'Marks' : [95,89,np.nan,98,90]
}
# Create a DataFrame
students = pd.DataFrame(data)
# Calculate the average marks
average_marks = students['Marks'].mean()

# Fill NaN in the Marks column with the average marks
students['Marks'] = students['Marks'].fillna(average_marks)

print("Updated DataFrame:")
print(students)



# 14.Drop Missing Values
# oDrop rows where any NaN occurs.
import pandas as pd
import numpy as np
# Create a dictionary with data
data = { 'Name': ['Sumedh','Piyush','Prasad','Sachin','Aditya'],
    'Age' : [18,19,np.nan,19,np.nan] , 
    'Marks' : [95,89,np.nan,98,90]
}
# Create a DataFrame
students = pd.DataFrame(data)
students = students.dropna(how='any')

print("Updated DataFrame:")
print(students)



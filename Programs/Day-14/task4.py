import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}
df = pd.DataFrame(data)




#Selecting a column
print("select only the name column")
print(df['Name'])
print(df.Name)

# Selecting multiple columns
#print(df[['Name','Age']])

 #Selecting by position
#print(df.iloc[0])           # First row
#print(df.iloc[0, 1])        # First row, second column
print("selectct the first 3 rows")
print(df.iloc[0:3])    # First two rows, columns 1–2

#Selecting by label
print("\n people older than 30") 
print(df[df['Age']> 30])           # First row
#print(df.loc[0, 'Name'])    # Name of first person
#print(df.loc[0:1, ['Name','City']]) 

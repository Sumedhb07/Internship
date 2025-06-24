import pandas as pd
data = {
    'products': ['mobile', 'tv', 'laptop','cycle'],
    'price': [25000, 100000, 80000, 20000],
    'Stock': [20, 10, 15, 12]
}
df = pd.DataFrame(data)

print(df.to_string(index = False))

print(df.head())

#Last 5 rows
print(df.tail())

#Columns
print(df.columns)

#Info about data types
print(df.info())

#Statistical summary
print(df.describe())
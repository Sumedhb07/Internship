import pandas as pd
# Creating a DataFrame from a dictionary
data = {
    'products': ['mobile', 'tv', 'laptop','cycle'],
    'price': [25000, 100000, 80000, 20000],
    'Stock': [20, 10, 15, 12]
}
df = pd.DataFrame(data)

print(df.to_string(index = False))
import pandas as pd # type: ignore 

df = pd.read_csv('fruits_data.csv')
rows,colunm = df.shape

# df['apple(1kg)'] = df['apple(1kg)'].fillna(df['apple(1kg)'].mean())
# df['banana(1 dozen)'] = df['banana(1 dozen)'].fillna(df['banana(1 dozen)'].mean())
# df['mango(1kg)'] = df['mango(1kg)'].fillna(df['mango(1kg)'].median())
# df['grapes(1kg)'] = df['grapes(1kg)'].fillna(df['grapes(1kg)'].median())
# df['Water Melons(1)'].fillna('Not Available',inplace=True)
# print(df)

new_df= df.notna()
print(df)
print(new_df)
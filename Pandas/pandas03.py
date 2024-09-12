import pandas as pd # type: ignore

df = pd.read_csv('food_db.csv')
r,c = df.shape
print(r,c)
print(df)

new_df = df.replace(['10%','5%'],'13%')

print(new_df)

new_df2 = df.replace({
    'rating': {'Excellent':4,'Very Good':3,'Good':2,'Average':1}
})

print(new_df2)
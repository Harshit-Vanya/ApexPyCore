import pandas as pd   # type: ignore
df = pd.read_csv("movies_data.csv")
g = df.groupby('industry')

print(g.get_group("Hollywood"))


def grouper(df, idx, col):
    
    rating = df.at[idx, col] 

    if rating >= 8.0:
        return 'Excellent'
    elif 4.0 <= rating < 7.9:
        return 'Average'
    elif 1.0 <= rating < 3.9:
        return 'Poor'
    else:
        return 'others'
    

df['rating'] = [grouper(df, i, 'imdb_rating') for i in df.index]

print(df[['imdb_rating', 'rating']])

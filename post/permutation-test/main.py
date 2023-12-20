import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import jsonRW as jsRW

def numToCat(row):
    if row['userCritic_difference'] >= 30:
        return 'high'
    elif row['userCritic_difference'] >= 20:
        return 'moderate'
    else:
        return 'low'

metacritic_list = jsRW.readJson('updated_metacritic2019_data')
metacritic_dict = {'title':[], 'user_rating':[], 'critic_rating':[]}
for elem in metacritic_list:
    metacritic_dict['title'].append(elem['title'])
    metacritic_dict['user_rating'].append((elem['user_rating']))
    metacritic_dict['critic_rating'].append((elem['critic_rating']))
df = pd.DataFrame(metacritic_dict)

tbdIndex = (df[df['user_rating']=="tbd"].index)
df = df.drop(labels=tbdIndex, axis='index')
df['user_rating'] = pd.to_numeric(df['user_rating'])
df['critic_rating'] = pd.to_numeric(df['critic_rating'])
#print(df.dtypes)

df['user_rating'] = df['user_rating'] * 10

#df['user_rating_isDigit'] = df.apply(lambda x: x.loc['user_rating'].isdigit(), axis=1)
#print(df[df['user_rating_isDigit']==False])

#first_record = df.loc[0, ['user_rating', 'critic_rating']]
#print(first_record['user_rating'])

df['userCritic_difference'] = df.apply(lambda x: abs(x['user_rating']-x['critic_rating']), axis=1)
#print(df.loc[0:2, ['user_rating', 'critic_rating', 'userCritic_difference']])

df['difference_category'] = df.apply(lambda x: numToCat(x), axis=1)
df['difference_category'] = df['difference_category'].astype("category")
df['difference_category'] = df['difference_category'].cat.set_categories(["low", "moderate", "high"])
#print(df['difference_category'])
#print(df.loc[3:7, ['userCritic_difference', 'difference_category']])

print(df['userCritic_difference'].describe())
df_sorted = df.sort_values(axis=0, by='userCritic_difference', ascending=False)
print(df_sorted)
#print(df_sorted.loc[1:10])
print(df['userCritic_difference'].describe())
categories_count = (df.groupby('difference_category').size())
print(categories_count)

plt.close('all')
pie_series = pd.Series(categories_count, name='categories percentages')
pie_series.plot.pie(figsize=(6,6))
plt.show()

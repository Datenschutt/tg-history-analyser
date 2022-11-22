import pandas as pd
import csv
import numpy as np

group_name = input('Which group/channel name do you want to append? ')
keep = input('Please enter search term (one word only). ')
#load CSV as Dataframe in Pandas
df1 = pd.read_csv('chat_history.csv')


#Only these columns and there values are part of the resulting file.
df1 = df1[['id', 'type', 'date', 'date_unixtime', 'actor', 'actor_id', 'action',  'text', 'text_entities', 'from', 'from_id', 'photo']]

#add group_name column from the first input.
df = df1.assign(group_name=group_name)

#replace NaN with 0
df['actor'] = df['actor'].replace(np.nan, 0)
df['actor_id'] = df['actor_id'].replace(np.nan, 0)
df['action'] = df['action'].replace(np.nan, 0)
#df['members'] = df['members'].replace(np.nan, 0)
df['text'] = df['text'].replace(np.nan, 0)
df['text_entities'] = df['text_entities'].replace(np.nan, 0)
df['from'] = df['from'].replace(np.nan, 0)
df['from_id'] = df['from_id'].replace(np.nan, 0)



df_new = df[(df['text'].str.contains(keep) == True) | (df['text_entities'].str.contains(keep) == True)]
#neue CSV
df_new.to_csv('refined.csv')

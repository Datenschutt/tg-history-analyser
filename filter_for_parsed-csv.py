# This is the forked version of the 'filter.py'-script. The kept categories differ 
# from the standardversion. This script is applied for datasets, that have been 
# created by the 'parsing-channels.py'-script, to match the generated
# categories of the script. The input file name needs to be 
# 'parsed-data.csv' instead of 'chat_history.csv'. Keep that in mind if your
# executions are unsuccesfull. 


import pandas as pd
import csv
import numpy as np

group_name = input('Which group/channel name do you want to append? ')
keep = input('Please enter search term (one word only). ')
#load CSV as Dataframe in Pandas
df1 = pd.read_csv('parsed-data.csv')



#new categories

#Only these columns and there values are part of the resulting file.
df1 = df1[['message_nr', 'message_user', 'message_sent', 'message_reply_to_nr', 'message_text', 'message_has_photo', 'message_photo_link', 'message_has_video', 'message_video_link', 'parsed_file']]

#add group_name column from the first input.
df = df1.assign(group_name=group_name)

#keep only those mesages with the search word in the category 'message_text'
df_new = df[(df['message_text'].str.contains(keep) == True)]
#neue CSV
df_new.to_csv('refined.csv')

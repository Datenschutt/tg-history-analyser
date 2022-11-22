import pandas as pd
import json

#get the json-file. If the name is not "result.json" you have to change it manually
with open ('result.json',  "r", encoding="UTF-8") as f:
	data = json.loads(f.read())

#flattening nested json-list for "messages" and save to a csv- file named: 
#"full chat history.csv"
df = pd.json_normalize(data, record_path=['messages']) 
df.to_csv('chat_history.csv')



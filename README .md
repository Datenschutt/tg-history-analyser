Done by the people of Datenschutt (we are kind of in an early stage, so there is
no further public projects, yet. A homepage is also planned.)
In here you find 3 python scripts.

1.json_to_csv.py

2.json_to_html.py

3.filter.py

1.json_to_csv:This script requires a json-file, that is called 'result.json'. 
In our analysis of telegram data, we have always used the 'export chat history'-option in the telegram UI (desktop version). If you get the the 'result.json'-file 
the same way we did, everything should work. The output file is called 'chat_history.csv'

2.json_to_html.py: First you have to put in the file name, of the json-file you want to convert. It should be in the same directory from which you execute this python-script. After that you enter the desired name for the output file and the number of messages per html. We recommend  to test out how many messages per html-file work in your browser. Something between 5000-10000 should work. 

3.filter.py:  This script not only filters but also drops some of the categories of the input csv file. It only keeps 'id', 'type', 'date', 'date_unixtime', 'actor', 'actor_id', 'action',  'text', 'text_entities', 'from', 'from_id' and 'photo'.It requires a csv-file with the name 'chat_history.csv' for input. If you used script 2 (json_to_csv.py) everything is fine, since thats the standard file name thats used during the conversion.
After launching the script you may type in the group or channel name, which will be appended in an additional column, which can come in handy if you intend to merge datasets. After that you simply enter the term you want to search. Only one search term per filtering is possible. Another problem is that some letters and formatted writing (e.g. bold letters) look like gibberish. We are working on that... The scripts creates a new csv file with those messages, that contained the given search term in the columns 'text' or 'text_entities'. The output file is named 'refined.csv'

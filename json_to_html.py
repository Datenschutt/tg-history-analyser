import json
import math

def main(source_file='result.json', result_file='result.html', chunks=500):
	with open(source_file, 'r', encoding='utf-8') as r_file:
		content = json.load(r_file)
		messages = content['messages']

	# logic for multiple files
	message_lists = [messages[i:i+chunks] for i in range(0, len(messages), chunks)]
	print(f'Will write {len(message_lists)} files. Chunksize: {chunks}')

	# length of each file
	print('Length of each output file:')
	for liste in message_lists:
		print(len(liste))

	
	for number in range(0, len(message_lists)):
		# start building html
		html_string = '<!DOCTYPE html><html><head><meta charset="utf-8"/></head><body><div class="messages">'

		for msg in message_lists[number]:
			if msg['type'] == 'message':
				# build message head
				html_string += '<div class="message"><div class="message_head">'
				message_id = msg['id']
				from_user = msg['from']
				from_id = msg['from_id']
				time = msg['date']

				html_string += f'<p><b>id: </b>{message_id}, <b>from: </b>{from_user}, <b>from_id: </b>{from_id}, '

				# if message is forwarded
				if msg.get('forwarded_from', ''):
					forwarded_from = msg.get('forwarded_from')
					html_string += f'<b>forwarded_from: </b>{forwarded_from}, '

				# if message is a reply
				if msg.get('reply_to_message_id', ''):
					reply_to = msg.get('reply_to_message_id')
					html_string += f'<b>reply_to_message_id: </b>{reply_to}, '

				html_string += f'<b>time: </b>{time}</p></div><div class="message_body"><p class="text">'

				# build message body
				if type(msg.get('text')) == str:
					html_string += f'{msg.get("text")}'.replace('\n', '<br>')

				elif type(msg.get('text')) == list:
					for item in msg.get('text'):
						if type(item) == str:
							html_string += f'{item}'.replace('\n', '<br>')

						elif type(item) == dict:
							# handle bold text
							if item['type'] == 'bold':
								html_string += f'<b>{item["text"]}</b>'.replace('\n', '<br>')

							# handle italic
							elif item['type'] == 'italic':
								html_string += f'<i>{item["text"]}</i>'.replace('\n', '<br>')

							# handle underline
							elif item['type'] == 'underline':
								html_string += f'<u>{item["text"]}</u>'.replace('\n', '<br>')

							# handle preformatted text
							elif item['type'] == 'pre':
								html_string += f'<pre>{item["text"]}</pre>'.replace('\n', '<br>')

							# handle strikethrough
							elif item['type'] == 'strikethrough':
								html_string += f'<s>{item["text"]}</s>'.replace('\n', '<br>')

							# handle html code element
							elif item['type'] == 'code':
								html_string += f'<code>{item["text"]}</code>'.replace('\n', '<br>')

							# handle various items where only text is needed
							elif item['type'] in ['phone', 'hashtag', 'mention', 'email']:
								html_string += f'{item["text"]}'.replace('\n', '<br>')

							# handle user mentions
							elif item['type'] == 'mention_name':
								html_string += f'@{item["text"]}'.replace('\n', '<br>')

							# handle link
							elif item['type'] == 'link':
								html_string += f'<a href="{item["text"]}">{item["text"]}</a>'.replace('\n', '<br>')

							# handle text_link
							elif item['type'] == 'text_link':
								html_string += f'<a href="{item["href"]}">{item["text"]}</a>'.replace('\n', '<br>')

							# errorhandling if type is not supported
							else:
								print(item['type'], 'is not supported. Message Id: ', msg['id'])
				# close message div
				html_string += '</p><br>-----</div>'

		# after loop close messages div, html body and html tag
		html_string += '</div></body></html>'

		# write file
		with open(f'{result_file}_{number}.html', 'w', encoding='utf-8') as w_file:
			w_file.write(html_string)


# get user input for file names
source = str(input('sourcefile name: '))
result = str(input('resultfile name: '))
chunk = int(input('number of messages per html-file: '))

# get default if input == '' and check for correct suffix
if not source:
	source = 'result.json'
if source[-5:] != ".json":
	source += ".json"

if not result:
	result = 'result'
if result[-5:] == ".html":
	result = result[:-5]

# run program
main(source, result, chunk)
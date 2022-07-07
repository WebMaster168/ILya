from telethon.sync import TelegramClient
import csv

api_id =******** #your id telegram
api_hash = '***********************' #your hash in telegram
name = '@repteloed168' #your nickname in telegram
chat = 'from0to1com' #channel name

with TelegramClient(name, api_id, api_hash) as client:
    with open('final.csv', 'w', encoding='utf-8', newline='\n') as f:
        writer = csv.writer(f)
        for message in client.iter_messages(chat, reply_to=359, reverse=True): #reply_to specifies post id
            print(message.date, message.sender_id, message.text, '$')
            writer.writerow([message.date,message.sender_id,message.text, '$'])

# session kodni olish
# import os
# os.system('pip install telethon')
from telethon import TelegramClient, sync
from telethon.sessions import StringSession

# from telethon.errors import SessionaPasswordNeddedError
# my.telegram.org saytidan olish mumkin yoki birovniki ham boladi
api_id = int(input())
api_hash = ""
angestrum = input('enterni bosing')
with TelegramClient(StringSession(angestrum), api_id, api_hash) as client:
    client.send_message('me', client.session.save())

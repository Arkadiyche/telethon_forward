from telethon import TelegramClient, sync, events
from telethon.tl.types import PeerUser, PeerChat, PeerChannel

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
print("Введите свой api_id:")
api_id = int(input())
print("Введите свой api_hash:")
api_hash = input()

client = TelegramClient('session_name', api_id, api_hash)


client.start()

all_dialogs = client.get_dialogs()
for i, dialog in enumerate(all_dialogs):
    print(i, dialog.name),

print('Откуда подслушывать:')
chat_from = int(input())
print('Куда пересылать:')
chat_to = int(input())

@client.on(events.NewMessage(chats=(all_dialogs[chat_from])))
async def normal_handler(event):
    await client.forward_messages(all_dialogs[chat_to], event.message)


client.run_until_disconnected()

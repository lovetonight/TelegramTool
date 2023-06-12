from telethon import TelegramClient, events, sync
import time

from telethon.errors.rpcerrorlist import PeerIdInvalidError
# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.

api_id1 = 22580886
api_hash1 = '261cc9f72021203da950043327e7ee0c'
# The first parameter is the .session file name (absolute paths allowed)

# client1.send_message('testtelethonz', 'Hello! Talking to you from Telethon')
# https://t.me/CHINCRYPTO_NEWS
username = 'Teletool_Group'
chat_id = 0

client1 = TelegramClient('./session/session_name1', api_id1, api_hash1)
client1.start()
clients = {client1}  # Các account


for client in clients:
    try:
        entity = client.get_entity(username)
        chat_id = entity.id
        # Lấy tất cả tin nhắn (không giới hạn số lượng)
        messages = client.iter_messages(entity, limit=5)
        reply_message = 'Hello'  # Kịch bản nhắn tin
        message_ids = [msg.id for msg in messages]
        # client.delete_messages(entity, message_ids)
        client.send_message(entity, reply_message, reply_to=3)
        # time.sleep(2)
    except ValueError:
        print("Chat ID không hợp lệ")
    except Exception as e:
        print(f"Lỗi khi lấy nội dung cuộc trò chuyện: {str(e)}")

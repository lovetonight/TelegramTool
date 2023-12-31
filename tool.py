import datetime
from telethon import TelegramClient, events, sync
import random
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import GetMessagesRequest


from telethon.errors.rpcerrorlist import PeerIdInvalidError
# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
'''
api_id = 22580886
api_hash = '261cc9f72021203da950043327e7ee0c'
'''

# The first parameter is the .session file name (absolute paths allowed)

# client1.send_message('testtelethonz', 'Hello! Talking to you from Telethon')
# https://t.me/CHINCRYPTO_NEWS
username = 'Teletool_Group'
chat_id = 0


'''
client1 = TelegramClient(
    './session/+84 354529271', api_id=1, api_hash='api_hash')
client1.start()
clients = {client1}  # Các account
'''

'''
Lấy toàn bộ tin nhắn từ start_id tới end_id
username: username của người dùng hoặc group

'''




def getMessage(client, username, start_id, end_id):
    try:

        entity = client.get_entity(username)
        chat_id = entity.id
        # TODO: Chỉnh limit sao cho hợp lý
        messages = client.get_messages(entity, limit=1000)
        message_ids = [msg.id for msg in messages]
        for message in messages:
            if message.id >= start_id and message.id <= end_id:
                print(message.message)

    except ValueError:
        print("Chat ID không hợp lệ")
    except Exception as e:
        print(f"Lỗi khi lấy nội dung cuộc trò chuyện: {str(e)}")

    return


'''
Gửi/ xóa tin nhắn tới user hoặc group

Gửi tin nhắn có thể reply tin nhắn khác, bằng cách thay đổi 'reply_message_id' thành id của tin nhắn muốn reply

Delete tin nhắn trong trò chuyện với user có thể xóa tin nhắn của đối phương
'''

# for client in clients:
for i in range(1, 1000):
    i = i % 14
    if i == 7 or i == 0:
        continue
    index = str(i)
    client = TelegramClient('./session/session ('+index+').session',
                            api_id=1, api_hash='api_hash')
    print('./session/('+index+').session')
    client.start()
    try:
        entity = client.get_entity(username)
        chat_id = entity.id
        # Lấy tất cả tin nhắn (không giới hạn số lượng)

        messages = client.iter_messages(entity, limit=5)
        message_ids = [msg.id for msg in messages]
        # client.delete_messages(entity, message_ids)

        reply_message_id = 3
        reply_message = 'Hi guys!'  # Kịch bản nhắn tin
        list1 = [0, 1, 2, 3]
        script = ['Hello!', 'Good moring',
                  'Có tin gì mới không anh em', 'btc down quá']
        client.send_message(entity, script[random.choice(list1)],)
        # client.send_file(entity, 'img\demo.jpg')  # Send img

        # time.sleep(2)

    except ValueError:
        print("Chat ID không hợp lệ")
    except Exception as e:
        print(f"Lỗi khi lấy nội dung cuộc trò chuyện: {str(e)}")


'''
Tự động rep tin nhắn, áp dụng cho user
'''

# @client.on(events.NewMessage(pattern='(?i)hi|hello'))
# async def handler(event):
#    await event.reply('Hey!')

# client.run_until_disconnected()
# getMessage(client1, 'CHINCRYPTO_CHAT', 17622, 17647)

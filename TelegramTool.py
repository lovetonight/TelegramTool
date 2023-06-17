import asyncio
from telethon import TelegramClient
# from telethon.types import InputMediaSticker
import random
import json
import time


# Get Message
def GetMessage(client, username, start_id, end_id):
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


# Send Message
async def SendMessage(client, username, reply_message_id, messages):
    try:
        entity = await client.get_entity(username)
        message_per_turn = random.choice([1, 2, 3, 4])
        messages_send = random.sample(messages, message_per_turn)

        for message_send in messages_send:
            time.sleep(2)    
            await client.send_message(entity, message_send, reply_to=reply_message_id)
        return
    except ValueError:
        print("Chat ID không hợp lệ")
    except Exception as e:
        print(f"Lỗi khi lấy nội dung cuộc trò chuyện: {str(e)}")


# Delete Message
def DeleteMessage(client, username, limit_delete):
    try:
        entity = client.get_entity(username)
        messages = client.iter_messages(entity, limit_delete)
        message_ids = [msg.id for msg in messages]
        client.delete_messages(entity, message_ids)
    except ValueError:
        print("Chat ID không hợp lệ")
    except Exception as e:
        print(f"Lỗi khi xóa nội dung cuộc trò chuyện: {str(e)}")


def main():

    # username, chat_id
    username = 'GatherNetworkVietnam'
    reply_message_id = 0
    client = TelegramClient('./session/session (1).session',
                            api_id=1, api_hash='api_hash')
    client.start()

    client_2 = TelegramClient('./session/session (2).session',
                            api_id=1, api_hash='api_hash')
    client_2.start()

    client_3 = TelegramClient('./session/session (3).session',
                            api_id=1, api_hash='api_hash')
    client_3.start()

    client_4 = TelegramClient('./session/session (4).session',
                            api_id=1, api_hash='api_hash')
    client_4.start()

    client_5 = TelegramClient('./session/session (5).session',
                            api_id=1, api_hash='api_hash')
    client_5.start()

    json_file = open('./script/script.json', encoding="utf8")

    data = json.load(json_file)

    clients = [client, client_2, client_3, client_4, client_5]
    clients_index = [0, 1, 2, 0, 3, 4, 1, 3, 4, 2]
    index = 0

    for messages in data:
        time.sleep(20)    
        loop = asyncio.get_event_loop()
        loop.run_until_complete(SendMessage(clients[clients_index[index]], username, reply_message_id, messages))    
        index += 1      
    
    json_file.close()

if __name__ == "__main__":
    main()

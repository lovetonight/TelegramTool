import asyncio
from telethon import TelegramClient
# from telethon.types import InputMediaSticker
import random


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
async def SendMessage(client, username, reply_message_id):
    try:
        entity = await client.get_entity(username)
        reply_message = 'Hi guys!'  # Kịch bản nhắn tin
        list1 = [0, 1, 2, 3]
        script = ['Hello!', 'Good morning',
                  'Có tin gì mới không anh em', 'btc down quá']

        # send message
        await client.send_message(
            entity, script[random.choice(list1)], reply_to=reply_message_id)

        # send file
        await client.send_file(
            entity, './sticker/webm/2.webm', reply_to=reply_message_id)
        # client.send_file(entity, 'img\demo.jpg')  # Send img
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
    username = 'Teletool_Group'
    chat_id = 0
    reply_message_id = 0
    client = TelegramClient('./session/session (1).session',
                            api_id=1, api_hash='api_hash')
    client.start()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(SendMessage(client, username, reply_message_id))


if __name__ == "__main__":
    main()

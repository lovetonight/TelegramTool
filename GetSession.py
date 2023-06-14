from telethon import TelegramClient

api_id = int(input('Nhap api_id: '))
api_hash = input('Nhap api_hash: ')
phone = input('Nhap so dien thoai (VD:+84 359468511): ')
sessionpath = './session/' + phone
client = TelegramClient(sessionpath, api_id=api_id, api_hash=api_hash)
client.start(phone=phone)

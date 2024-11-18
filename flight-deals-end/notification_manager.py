import requests



class NotificationManager:

    def __init__(self):
        self.BOT_AUTH_TOKEN = "6419120328:AAGxCLUdTKKcQctIWoaEmZfcKuaHR_zD-Ws"
        self.TO_ID = "1609783808"

    def send_sms(self, message):
        send_text = 'https://api.telegram.org/bot' + self.BOT_AUTH_TOKEN + '/sendMessage?chat_id=' + self.TO_ID + '&parse_mode=Markdown&text=' + message
        response = requests.get(send_text)

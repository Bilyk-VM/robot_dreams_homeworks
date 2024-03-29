# Створюємо клас Bot
class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)


# Створюємо класс TelegramBot, який наслідує клас Bot
class TelegramBot(Bot):
    def __init__(self, name):
        super().__init__(name)
        self.url = None
        self.chat_id = None

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, message):
        print(f"{self.name} bot says {message} to chat {self.chat_id} using {self.url}")



some_bot = Bot('Marvin')
some_bot.say_name()
some_bot.send_message("Hello")

telegram_bot = TelegramBot("TG")
telegram_bot.say_name()

telegram_bot.set_chat_id(1)
telegram_bot.send_message('Hello')


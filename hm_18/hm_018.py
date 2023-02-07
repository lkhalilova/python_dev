# task_num_1
class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)

# task_num_2


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
        print(f"This telegram bot says {message} to chat {self.chat_id} using {self.url}")

# task_num_3


class MyStr(str):
    def __str__(self, *args, **kwargs):
        return str(self.upper())

# task_num_4


class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()


# task_num_5


def init_function(self, name):
    self.name = name


def say_name_function(self):
    print(self.name)


def send_message_function(self, message):
    print(message)


bot = type(
    "BotClass",
    (),
    {
        "__init__": init_function,
        "say_name": say_name_function,
        "send_message": send_message_function
    }
)


def set_url_function(self, url):
    self.url = url


def set_chat_id_function(self, chat_id):
    self.chat_id = chat_id


def send_message_function(self, message):
    print(f"This telegram bot says {message} to chat {self.chat_id} using {self.url}")


telegram_bot = type(
    "TelegramBotClass",
    (bot,),
    {
        "set_url": set_url_function,
        "set_chat_id": set_chat_id_function,
        "send_message": send_message_function
    }
)










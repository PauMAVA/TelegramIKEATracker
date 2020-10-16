from . import parser


class TelegramConfig:

    def __init__(self, bot_token, bot_username):
        self.bot_token = bot_token
        self.bot_username = bot_username


class DatabaseConfig:

    def __init__(self, address, port, user, password, database):
        self.address = address
        self.port = port
        self.user = user
        self.password = password
        self.database = database


class Config:

    def __init__(self, telegram, database):
        self.telegram = telegram
        self.database = database


current_path = None
current_config = None


def get_config(path):
    if current_path is not path:
        refresh_config(path)
    return current_config


def refresh_config(path):
    current_config = parser.parse_config(path)
    if current_config is not None:
        current_path = path
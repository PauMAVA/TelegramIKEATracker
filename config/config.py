from . import parser


class TelegramConfig:

    def __init__(self, bot_token, bot_username):
        self.bot_token = bot_token
        self.bot_username = bot_username

    def token(self):
        return self.bot_token

    def user(self):
        return self.bot_username


class DatabaseConfig:

    def __init__(self, address, port, user, password, database):
        self.address = address
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def address(self):
        return self.address

    def port(self):
        return self.port

    def user(self):
        return self.user

    def password(self):
        return self.password

    def database(self):
        return self.database


class Config:

    def __init__(self, telegram: TelegramConfig, database: DatabaseConfig):
        self.telegram = telegram
        self.database = database

    def telegram(self):
        return self.telegram

    def database(self):
        return self.database


current_path = None
current_config = None


def get_config(path):
    if current_path is not path:
        refresh_config(path)
    return current_config


def refresh_config(path):
    global current_config
    global current_path
    current_config = parser.parse_config(path)
    if current_config is not None:
        current_path = path

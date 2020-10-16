import toml
from . import config


REQUIRED_SECTIONS = ["telegram", "database"]
REQUIRED_KEYS = {
    "token": "telegram",
    "user": "telegram",
    "username": "database",
    "password": "database",
    "address": "database",
    "port": "database",
    "db": "database"
}


def parse_config(path):
    parsed = toml.load(path)
    missing_sections, missing_keys = check_format(parsed)
    if len(missing_sections) != 0:
        raise Exception("Config file " + path + " is missing the following sections: " + str(missing_sections))
    if len(missing_keys) != 0:
        raise Exception("Config file " + path + " is missing the following keys: " + str(missing_keys))
    return config.Config(
        telegram=config.TelegramConfig(
            bot_token=parsed['telegram']['token'],
            bot_username=parsed['telegram']['user']
        ),
        database=config.DatabaseConfig(
            address=parsed['database']['address'],
            port=parsed['database']['port'],
            user=parsed['database']['username'],
            password=parsed['database']['password'],
            database=parsed['database']['db']
        )
    )


def check_format(parsed):
    missing_sections = []
    missing_keys = {}
    for section in REQUIRED_SECTIONS:
        if section not in parsed:
            missing_sections.append(section)
    for key, section in REQUIRED_KEYS.items():
        if section not in missing_sections:
            if key not in parsed[section]:
                if section not in missing_keys:
                    missing_keys[section] = []
                missing_keys[section].append(key)
    return missing_sections, missing_keys

from config import config
from bot import ikeabot


def main():
    print("Starting bot-ikea-tracker")
    current_config: config.Config = config.get_config('appconfig.toml')
    ikeabot.start(current_config.telegram)


if __name__ == '__main__':
    main()

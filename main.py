from config import config


def main():
    print("Starting telegram-ikea-tracker")
    current_config = config.get_config('appconfig.toml')



if __name__ == '__main__':
    main()

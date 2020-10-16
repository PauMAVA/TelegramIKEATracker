from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from config.config import TelegramConfig

updater: Updater = None
username: str = ""


def start(telegram_config: TelegramConfig):
    global updater
    global username
    token = telegram_config.token()
    user = telegram_config.user()
    if token is None or user is None:
        raise Exception("Bot token and username parameters cannot be None!")
    updater = Updater(token)
    username = user
    register_commands()
    updater.start_polling()
    updater.idle()


def register_commands():
    for handler in command_handlers:
        updater.dispatcher.add_handler(handler)


def start_cmd(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Welcome {update.effective_user.username},\n"
                              f"\n"
                              f"🎉 I am glad you have decided to join this service!\n"
                              f"\n"
                              f"\u2139\uFE0F Info\n"
                              f"Here you will be able to track IKEA products for availability and configure periodic "
                              f"reports so that you will never miss great buy opportunities.\n "
                              f"\n"
                              f"\u2328\uFE0F Commands\n"
                              f"Let's start {update.effective_user.username}! Try some of this commands: \n"
                              + get_commands_message()
                              + f"\n"
                              f"I recommend that you start by typing the /quickstart command.\n"
                              f"\n"
                              f"😀 Thanks for joining {update.effective_user.username}!")


def help_cmd(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("\u2757 I've heard you need help!\n"
                              "\n"
                              "Here you have a list of all available commands:\n"
                              + get_commands_message())


def get_commands_message():
    return f"/help -> Displays the available commands.\n" \
           f"/quickstart -> Set up your preferences and initial configuration.\n" \
           f"/track -> Create a new tracking.\n" \
           f"/report -> Create a new periodic report.\n" \
           f"/delete -> Delete trackings or/and reports.\n" \
           f"/current -> Gets all the current tracking states.\n" \
           f"/lookup -> Check the current availability of an item without creating a tracking.\n"


command_handlers = [
    CommandHandler('start', start_cmd),
    CommandHandler('help', help_cmd)
]
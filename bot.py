#...

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

def main():
    updater = Updater("337618195:AAFlOtkSrbEyf4xkYUpFt2kEHNZWHM1BV-Q")
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler((Filters.text), talk_to_me))

    dp.add_error_handler(show_error)

    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
    print('Привет! /start')
    print(update)
    bot.sendMessage(update.message.chat_id, text="Давай общаться!")

def show_error(bot, update, error):
    print(error)

def talk_to_me(bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text)

main()

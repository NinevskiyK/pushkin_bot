import logging
import telegram
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler,  Filters, ConversationHandler)

TOKEN = open('key.txt').read()

def start(bot, update):
    update.message.reply_text("Hello. Write Text.")
def predict(data):
    return "Hello!"
def get_text(bot, update):
    data = bot.message.text()
    bot.message.reply_text(data)

def main():
    my_bot = Updater(TOKEN, use_context = True)
    my_bot.dispatcher.add_handler(CommandHandler('start', start))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, get_text))
    my_bot.start_polling()
    my_bot.idle()

if (__name__ == '__main__'):
    main()
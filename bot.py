import logging
import telegram
from telegram.ext import (Updater, CommandHandler, MessageHandler,  Filters, ConversationHandler)

TOKEN = open('key.txt').read()
def start(bot, update):
    bot.message.reply_text("Hello. Write Text.")
def Make_continue(bot, update):
    bot.message.reply_text(bot.message.text)

def main():
    my_bot = Updater(TOKEN)
    my_bot.dispatcher.add_handler(CommandHandler('start', start))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, Make_continue))
    my_bot.start_polling()
    my_bot.idle()

main()
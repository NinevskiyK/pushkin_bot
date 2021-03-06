import logging
import telegram
from telegram.ext import (Updater, CommandHandler, MessageHandler,  Filters, ConversationHandler)
from Engine import make_continue_markovify
TOKEN = open('key.txt').read()
def start(bot, update):
    bot.message.reply_text("Привет! Напиши мне начало стиха, а я его продолжу!")
def Make_continue(bot, update):
    try:
        with open("log.txt", "a") as fl:
            s =("User: " + str(bot.message.chat.username) + ', ' + str(bot.message.chat.first_name) + ', ' + str(bot.message.chat.last_name) + \
             " Message: " + str(bot.message.text))
            fl.writelines(s + '\n')
    except:
        with open("log.txt", "a") as fl:
            s =("User: " + str(bot.message.chat.username) + ', ' + str(bot.message.chat.first_name) +  \
             " Message: " + str(bot.message.text))
            fl.writelines(s + '\n')
    bot.message.reply_text(make_continue_markovify(bot.message.text))

def main():
    my_bot = Updater(TOKEN)
    my_bot.dispatcher.add_handler(CommandHandler('start', start))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, Make_continue))
    my_bot.start_polling()
    my_bot.idle()

main()
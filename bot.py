import telebot
import time

TOKEN = "6014737525:AAEnRcfIZmruG_9TzZNRmJUhnZkKTn36QnU"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    print(message.text)


@bot.message_handler(commands=["hello","hi"])
def hello(message):
    bot.send_message(message.chat.id,"HELLO WORLD")

@bot.message_handler(commands=["fb"])
def fb(message):
    bot.send_message(message.chat.id,"git clone")
@bot.message_handler(commands=["public"])
def pulic(message):
    bot.send_message(message.chat.id,"on working")
while True:
    try:
        bot.polling()
    except:
        time.sleep(5)

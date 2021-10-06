import os
import telebot

API_KEY=os.getenv('api')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message, "Hey! Hows it going?")


@bot.message_handler(commands=['hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello!")

@bot.message_handler(commands=['start', 'help','hello'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=['document', 'audio','photo'])
def handle_docs_audio_photo(message):
	bot.send_message(message.chat.id, "Beatiful!")

@bot.message_handler()
def echo_all(message):
	bot.reply_to(message,"SOSI MOY HUI")


bot.infinity_polling()
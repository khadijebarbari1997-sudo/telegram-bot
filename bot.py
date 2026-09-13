import telebot 

bot = telebot.TeleBot("put_your_tocken_here")

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message, "Hello I'm Your First Botg"

@bot.message_handler(func=lambda message:True)
 def echo_all(message) :
  bot.reply_to(message, message.text)

bot.polling()

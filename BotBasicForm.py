import telebot

bot = telebot.Telebot("8944329944:AAGaNhNLNJhhC8L1viXOVbmH7ncfisyU55U")

@bot.message_handler(commands=['start']
                     def send_welcome(message):
                       bot.reply_to(messsage, "Hello !I'm your firstbot!")
@bot.message_handler(func=lambda message:True)
                     def echo_all(message):
                       bot.reply_to(message,message.text)
bot.polling()

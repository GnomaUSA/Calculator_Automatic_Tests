import telebot
TOKEN = '6865155759:AAHDlLsRPigdUr_LneqvTx_x3Q7B4tT7eEU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")

@bot.message_handler(content_types=['photo'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

bot.polling(none_stop=True)

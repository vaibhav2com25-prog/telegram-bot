import os
import telebot
from telebot import types

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        types.KeyboardButton("🇮🇳 India Number Info"),
        types.KeyboardButton("🚗 Vehicle Info")
    )
    markup.add(
        types.KeyboardButton("🆔 Aadhaar Info"),
        types.KeyboardButton("👨‍👩‍👧 Aadhaar to Family Info")
    )
    markup.add(
        types.KeyboardButton("💳 My Credits"),
        types.KeyboardButton("📞 Contact Admin")
    )

    bot.send_message(
        message.chat.id,
        "✅ Choose an option below to begin!",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def menu(message):
    bot.send_message(message.chat.id, "✅ Button received")

bot.infinity_polling()
  

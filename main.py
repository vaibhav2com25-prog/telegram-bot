from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("8537887755:AAGePD_nlARncv3WY4HMDRMfCVAMqnrCh6I")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔥 Get Premium", url="https://example.com")],
        [InlineKeyboardButton("📞 Support", url="https://t.me/yourusername")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "What can this bot do?\n\nClick button below 👇",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot started...")
app.run_polling()

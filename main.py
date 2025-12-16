import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("8537887755:AAGePD_nlARncv3WY4HMDRMfCVAMqnrCh6I")

if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("✅ Click Me", callback_data="btn_click")],
        [InlineKeyboardButton("🌐 Open Google", url="https://google.com")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome!\nNeeche button par click kijiye 👇",
        reply_markup=reply_markup
    )

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("🎉 Button successfully clicked!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    explain_handlers = [
        CommandHandler("start", start)
    ]

    from telegram.ext import CallbackQueryHandler
    app.add_handler(CallbackQueryHandler(button_click))
    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == "__main__":
    main()
    

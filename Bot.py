from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from deep_translator import GoogleTranslator

BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text

    try:
        translated = GoogleTranslator(
            source="auto",
            target="en"
        ).translate(text)

        await update.message.reply_text(
            f"English Translation:\n{translated}"
        )

    except:
        await update.message.reply_text(
            "Translation failed."
        )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT, reply)
)

app.run_polling()

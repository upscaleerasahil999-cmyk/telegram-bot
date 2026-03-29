import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ─── CONFIG ────────────────────────────────────────────────────────────────────
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# ─── LOGGING ───────────────────────────────────────────────────────────────────
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ─── RESPONSES ─────────────────────────────────────────────────────────────────

async def send_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    await update.message.reply_text(
        f"👋 Hello, {name}! Welcome to *Your Business Name*.\n\n"
        "I'm here to help you. Just type any of these words:\n\n"
        "📞 *contact* — Get our contact information\n"
        "💰 *price* — View our pricing plans\n"
        "🆓 *support* — Free support & assistance\n"
        "❓ *help* — Show all commands\n\n"
        "No need to type / before the word 😊",
        parse_mode="Markdown"
    )

async def send_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 *Contact Us*\n\n"
        "🏢 *Company:* Your Business Name\n"
        "📧 *Email:* contact@yourbusiness.com\n"
        "📱 *Phone:* +1 (234) 567-8900\n"
        "🌐 *Website:* https://www.yourbusiness.com\n"
        "📍 *Address:* 123 Main Street, City, Country\n\n"
        "🕐 *Working Hours:* Mon–Fri, 9 AM – 6 PM\n\n"
        "We typically respond within 24 hours. 😊",
        parse_mode="Markdown"
    )

async def send_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 *Our Pricing Plans*\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🥉 *Basic Plan — $9/month*\n"
        "  ✅ Feature one\n"
        "  ✅ Feature two\n"
        "  ✅ Feature three\n\n"
        "🥈 *Standard Plan — $29/month*\n"
        "  ✅ Everything in Basic\n"
        "  ✅ Feature four\n"
        "  ✅ Feature five\n\n"
        "🥇 *Premium Plan — $79/month*\n"
        "  ✅ Everything in Standard\n"
        "  ✅ Priority support\n"
        "  ✅ Unlimited access\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📩 For custom pricing, type *contact*",
        parse_mode="Markdown"
    )

async def send_support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆓 *Free Support*\n\n"
        "We offer *free support* for all our users!\n\n"
        "💬 *Live Chat:* Available on our website\n"
        "📧 *Email:* support@yourbusiness.com\n"
        "📖 *Docs:* https://docs.yourbusiness.com\n"
        "🎥 *Tutorials:* https://youtube.com/yourchannel\n\n"
        "Our support team is ready to assist you — *completely free of charge!* 🎉",
        parse_mode="Markdown"
    )

async def send_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❓ *Help — Available Keywords*\n\n"
        "Just type any of these words:\n\n"
        "📞 *contact* — Our contact details\n"
        "💰 *price* — View our pricing plans\n"
        "🆓 *support* — Free support resources\n"
        "❓ *help* — Show this help message\n\n"
        "💡 No need to use / before any word!",
        parse_mode="Markdown"
    )

# ─── KEYWORD HANDLER ───────────────────────────────────────────────────────────

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower().strip()

    if any(word in text for word in ["start", "hi", "hello", "hey"]):
        await send_start(update, context)
    elif "contact" in text:
        await send_contact(update, context)
    elif "price" in text or "pricing" in text or "cost" in text or "plan" in text:
        await send_price(update, context)
    elif "support" in text or "help" in text or "assist" in text:
        await send_support(update, context)
    else:
        await update.message.reply_text(
            "🤔 I didn't understand that.\n\n"
            "Try typing one of these:\n"
            "👉 *contact*, *price*, *support*, *help*",
            parse_mode="Markdown"
        )

# ─── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN environment variable is not set!")

    app = Application.builder().token(BOT_TOKEN).build()

    # Slash commands still work too
    app.add_handler(CommandHandler("start",   send_start))
    app.add_handler(CommandHandler("contact", send_contact))
    app.add_handler(CommandHandler("price",   send_price))
    app.add_handler(CommandHandler("support", send_support))
    app.add_handler(CommandHandler("help",    send_help))

    # Keyword handler — no slash needed
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

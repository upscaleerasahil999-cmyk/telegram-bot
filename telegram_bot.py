import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ─── CONFIG ────────────────────────────────────────────────────────────────────
# On Railway, set BOT_TOKEN as an Environment Variable (never hardcode it)
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# ─── LOGGING ───────────────────────────────────────────────────────────────────
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ─── COMMAND HANDLERS ──────────────────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    await update.message.reply_text(
        f"👋 Hello, {name}! Welcome to *Your Business Name*.\n\n"
        "I'm here to help you. Here's what I can do:\n\n"
        "📞 /contact — Get our contact information\n"
        "💰 /price — View our pricing plans\n"
        "🆓 /support — Free support & assistance\n"
        "❓ /help — Show all commands\n\n"
        "How can I help you today?",
        parse_mode="Markdown"
    )


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
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


async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        "📩 For custom pricing, use /contact",
        parse_mode="Markdown"
    )


async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
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


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❓ *Help — Available Commands*\n\n"
        "/start — Welcome message & overview\n"
        "/contact — Our contact details\n"
        "/price — View our pricing plans\n"
        "/support — Free support resources\n"
        "/help — Show this help message\n\n"
        "💡 Tap any command above to use it!",
        parse_mode="Markdown"
    )


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤔 Sorry, I didn't understand that.\n\n"
        "Please use /help to see all available commands."
    )


# ─── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN environment variable is not set!")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start",   start))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("price",   price))
    app.add_handler(CommandHandler("support", support))
    app.add_handler(CommandHandler("help",    help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))

    logger.info("Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8749317542:AAHE1UwFWU0Ygn36Dc4v1lc9zN1GVhz5fi0"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Inkubator 🏢", callback_data="inkubator")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Добро пожаловать! Выберите раздел:",
        reply_markup=reply_markup
    )

# обработка кнопок
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "inkubator":
        keyboard = [
            [InlineKeyboardButton("110 talik", callback_data="100")],
            [InlineKeyboardButton("130 talik", callback_data="130")],
            [InlineKeyboardButton("72 talik", callback_data="72")],
            [InlineKeyboardButton("50 talik", callback_data="50")]
        ]
        await query.edit_message_text(
            "Выберите инкубатор:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # 110
    elif query.data == "100":
        await query.message.reply_photo(
            photo="https://ibb.co/1f8jyKpx",
            caption="""110 talik inkubator:
100% Avtomatik boshqaruv
Ishlash: 220-12 volt
Avtomatik tuxumni aylantirish
Murojaat: +998996551557
Toshkent sh."""
        )

    # 130
    elif query.data == "130":
        await query.message.reply_photo(
            photo="https://ibb.co/1f8jyKpx",
            caption="""130 talik inkubator:
100% Avtomatik boshqaruv
Ishlash: 220-12 volt
Avtomatik tuxumni aylantirish
Murojaat: +998996551557
Toshkent sh."""
        )

    # 72
    elif query.data == "72":
        await query.message.reply_photo(
            photo="https://ibb.co/1f8jyKpx",
            caption="""72 talik inkubator:
100% Avtomatik boshqaruv
Ishlash: 220-12 volt
Avtomatik tuxumni aylantirish
Murojaat: +998996551557
Toshkent sh."""
        )

    # 50
    elif query.data == "50":
        await query.message.reply_photo(
            photo="https://ibb.co/1f8jyKpx",
            caption="""50 talik inkubator:
100% Avtomatik boshqaruv
Ishlash: 220-12 volt
Avtomatik tuxumni aylantirish
Murojaat: +998996551557
Toshkent sh."""
        )

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CallbackQueryHandler(button))

updater.start_polling()
updater.idle()

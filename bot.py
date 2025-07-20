from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Головне меню
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("1️⃣ Як оформити підписку на модпак", callback_data="sub_info")],
        [InlineKeyboardButton("2️⃣ Де дізнатись більше про модпак", callback_data="modpack_info")],
        [InlineKeyboardButton("3️⃣ Соцмережі проєкта Carleo Place", callback_data="socials")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привіт! Обери, що тебе цікавить:", reply_markup=reply_markup)

# Обробка кнопок
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "sub_info":
        keyboard = [
            [InlineKeyboardButton("🔗 Перейти на Boosty", url="https://boosty.to/твій_акаунт")],
            [InlineKeyboardButton("💸 Як оплатити через TON", callback_data="ton_help")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="main_menu")]
        ]
        await query.edit_message_text("Оформлення підписки:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "ton_help":
        await query.edit_message_text(
            "🪙 Щоб оплатити через TON, перейдіть на сайт з підтримкою TON-гаманців (наприклад, [Tonkeeper](https://tonkeeper.com)) "
            "та скануйте QR-код або відправте кошти на адресу, вказану на Boosty.",
            parse_mode='Markdown',
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Назад", callback_data="sub_info")]])
        )

    elif query.data == "modpack_info":
        keyboard = [
            [InlineKeyboardButton("💬 Discord сервер", url="https://discord.gg/твій_сервер")],
            [InlineKeyboardButton("📢 Telegram група", url="https://t.me/твоя_група")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="main_menu")]
        ]
        await query.edit_message_text("Інформація про модпак:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "socials":
        keyboard = [
            [InlineKeyboardButton("💬 Discord", url="https://discord.gg/твій_сервер")],
            [InlineKeyboardButton("🎵 TikTok", url="https://tiktok.com/@твій_аккаунт")],
            [InlineKeyboardButton("📢 Telegram", url="https://t.me/твій_канал")],
            [InlineKeyboardButton("📺 YouTube", url="https://youtube.com/@твій_канал")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="main_menu")]
        ]
        await query.edit_message_text("Соцмережі Carleo Place:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "main_menu":
        await start(update, context)

# Запуск
import os
app = ApplicationBuilder().token(os.environ["BOT_TOKEN]).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()

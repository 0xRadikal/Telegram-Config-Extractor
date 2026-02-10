import logging
import requests
import base64
import io
import os  # اضافه شده برای تنظیم پروکسی سیستمی
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# --- تنظیمات ---
TOKEN = "BOT_TOKEN_HERE"
CHANNEL_ID = "@Raydikalx"
CHANNEL_URL = "https://t.me/Raydikalx"

# --- تنظیمات پروکسی (Karing) ---
# این روش تمام ترافیک برنامه را مجبور می‌کند از Karing رد شود
PROXY_URL = "http://127.0.0.1:3067"
os.environ["HTTP_PROXY"] = PROXY_URL
os.environ["HTTPS_PROXY"] = PROXY_URL

# تنظیمات لاگ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- توابع کمکی ---

def decode_sub_link(url):
    try:
        # چون پروکسی رو در os.environ ست کردیم، requests خودکار از همون استفاده میکنه
        # اما برای اطمینان هدر یوزر ایجنت رو میذاریم
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        response = requests.get(url, timeout=15, headers=headers)
        response.raise_for_status()
        encoded_data = response.text.strip()
        
        # اصلاح پدینگ Base64
        missing_padding = len(encoded_data) % 4
        if missing_padding:
            encoded_data += '=' * (4 - missing_padding)
            
        decoded_bytes = base64.b64decode(encoded_data)
        decoded_text = decoded_bytes.decode('utf-8')
        
        configs = [line.strip() for line in decoded_text.splitlines() if line.strip()]
        return configs
    except Exception as e:
        print(f"Error decoding: {e}")
        return None

async def check_membership(user_id, bot):
    # فعلا همیشه True
    return True

# --- هندلرها ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"--- Command /start received from {update.effective_user.first_name} ---")
    
    keyboard = [
        [KeyboardButton("📥 استخراج کانفیگ"), KeyboardButton("👤 حساب کاربری")],
        [KeyboardButton("📞 پشتیبانی"), KeyboardButton("ℹ️ راهنما")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "سلام! ربات آنلاین شد ✅\nالان لینک سابت رو بفرست تا تست کنیم.",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    print(f"--- Message received: {text} ---")
    
    if text == "📥 استخراج کانفیگ":
        await update.message.reply_text("لینک رو بفرست:")
        
    elif text.startswith("http"):
        status_msg = await update.message.reply_text("⏳ در حال پردازش...")
        configs = decode_sub_link(text)
        
        if configs:
            file_content = "\n".join(configs)
            file_buffer = io.BytesIO(file_content.encode('utf-8'))
            file_buffer.name = "configs.txt"
            
            await status_msg.edit_text(f"✅ تعداد {len(configs)} کانفیگ پیدا شد.")
            await update.message.reply_document(
                document=file_buffer, 
                caption="📂 بفرما اینم فایل کانفیگ‌ها\n🤖 @configexBot",
                reply_to_message_id=update.message.message_id
            )
        else:
            await status_msg.edit_text("❌ نتونستم لینک رو باز کنم. شاید فیلتره یا لینک خراب شده.")
    else:
        await update.message.reply_text("پیامت رو گرفتم: " + text)

# --- اجرا ---

if __name__ == '__main__':
    print(f"Bot is starting with Proxy (Env): {PROXY_URL} ...")
    
    # دیگر نیازی به تنظیمات پیچیده پروکسی در اینجا نیست
    # چون در خطوط اول کد با os.environ ست شده است
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
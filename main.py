import telebot
import os

# আপনার Bot Token এখানে দিন
API_TOKEN = '8162300316:AAFh9rxCwRCyG_8st09sooJIU78fLg0md-c'
bot = telebot.TeleBot(API_TOKEN)

# ডেটাবেস হিসেবে ডিকশনারি (Render এ চললে সাময়িকভাবে ইউজারের আইডি মনে রাখবে)
connected_devices = {}

@bot.message_handler(commands=['start'])
def start(message):
    help_text = (
        "👋 Welcome to Mobile Remote Sentinel!\n\n"
        "আপনার ফোন কানেক্ট করতে নিচে কমান্ডটি কপি করে Termux এ রান করুন:\n\n"
        f"`curl -sL https://raw.githubusercontent.com/YOUR_USER_NAME/YOUR_REPO/main/setup.sh | bash`"
    )
    bot.reply_to(message, help_text, parse_mode='Markdown')

@bot.message_handler(commands=['snap', 'loc', 'battery'])
def handle_remote_commands(message):
    user_id = message.from_user.id
    # এখানে আমরা ইউজারের ফোনে কমান্ড সিগন্যাল পাঠাবো
    bot.reply_to(message, f"⌛ Sending {message.text} command to your device...")
    # (অ্যাডভান্সড লজিক: এখানে সকেট বা রিয়েল টাইম ডেটাবেস দিয়ে ফোনের স্ক্রিপ্টকে ট্রিগার করা হয়)

bot.polling()

import telebot
import os
from flask import Flask
from threading import Thread

# আপনার Bot Token
API_TOKEN = '8162300316:AAFh9rxCwRCyG_8st09sooJIU78fLg0md-c'
bot = telebot.TeleBot(API_TOKEN)

# Render এর পোর্ট এরর ঠিক করার জন্য ছোট একটি ওয়েব সার্ভার
app = Flask('')

@app.route('/')
def home():
    return "Bot is Running!"

def run():
    # Render অটোমেটিক পোর্ট নম্বর দেয়, সেটা না থাকলে ১০০০০ ব্যবহার করবে
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

@bot.message_handler(commands=['start'])
def start(message):
    setup_cmd = "curl -sL https://raw.githubusercontent.com/R8rAIHAN/R8rAIHAN_Mobile_Cam_bot/main/setup.sh | bash"
    bot.reply_to(message, f"মোবাইল কানেক্ট করতে এই কমান্ডটি কপি করে Termux এ দিন:\n\n`{setup_cmd}`", parse_mode='Markdown')

if __name__ == "__main__":
    keep_alive() # এটি পোর্টের সমস্যা সমাধান করবে
    print("Bot is polling...")
    bot.polling(none_stop=True)

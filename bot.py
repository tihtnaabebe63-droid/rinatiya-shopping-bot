
import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json or {}
    message = data.get("message", {})
    text = message.get("text", "")
    chat = message.get("chat", {})
    chat_id = chat.get("id")

    if text == "/start":
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": "እንኳን ወደ Rinatiya Shopping በደህና መጡ! 🛍️"
            " ትዕዛዝዎን ይላኩ።"
            }
        )

    return {"ok": True}

@app.route("/order", methods=["POST"])
def order():
    data = request.json or {}
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": "🛍️ New Order:\n" + str(data)
        }
    )
    return {"ok": True}

@app.route("/")
def home():
    return "Rinatiya Shopping Bot is running!"

if __name__ == "__main__":
    app.run()

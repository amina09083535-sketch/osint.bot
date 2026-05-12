import requests
import time
from osint import search_username

TOKEN = "8794029414:AAF_YoYqJzt0HYTEceN4aZ4vzuRytjMViYM"
URL = f"https://api.telegram.org/bot{TOKEN}"

offset = 0

print("Бот запущен...")

while True:
    try:
        r = requests.get(URL + f"/getUpdates?offset={offset}", timeout=10).json()

        for update in r.get("result", []):
            offset = update["update_id"] + 1

            msg = update.get("message", {})
            chat_id = msg.get("chat", {}).get("id")
            text = msg.get("text", "")

            if not chat_id:
                continue

            if text == "/start":
                requests.get(URL + f"/sendMessage?chat_id={chat_id}&text=OSINT бот работает ✅")

            elif text.startswith("/username"):
                username = text.replace("/username", "").strip()

                result = search_username(username)
                answer = "\n".join(result)

                requests.get(URL + f"/sendMessage?chat_id={chat_id}&text={answer}")

    except Exception as e:
        print("error:", e)

    time.sleep(1)

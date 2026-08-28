import os
import json
import requests

PARSE_API_KEY = os.environ["PARSE_API_KEY"]
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHANNEL_ID = os.environ.get("TELEGRAM_CHANNEL_ID", "@BIGBASKETDEALSINDIA")

API_BASE = "https://api.parse.bot/scraper/1d9ca2c5-176c-4bc0-9cf3-db9056850958"

PRODUCT_SLUG = "zeeba-everyday-super-mongra-basmati-rice-pure-authentic-delicious-taste-unique-aroma-5-kg"

STATE_FILE = "price_state.json"


def get_product():
    url = f"{API_BASE}/search_products"

    params = {
        "page": 1,
        "query": "Zeeba Everyday Super Mongra Basmati Rice 5 kg"
    }

    headers = {
        "X-API-Key": PARSE_API_KEY
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=30
    )

    response.raise_for_status()
    return response.json()


def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        json={
            "chat_id": CHANNEL_ID,
            "text": message,
            "disable_web_page_preview": False
        },
        timeout=30
    )

    response.raise_for_status()


def load_state():
    if not os.path.exists(STATE_FILE):
        return None

    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(data):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def main():
    data = get_product()

    print("BigBasket API response received.")
    print(json.dumps(data, indent=2)[:5000])

    # Product matching and price extraction will be finalized
    # after confirming the exact API response structure.


if __name__ == "__main__":
    main()

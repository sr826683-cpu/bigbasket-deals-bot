import os
import json
import requests

PARSE_API_KEY = os.environ["PARSE_API_KEY"]
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHANNEL_ID = os.environ.get(
    "TELEGRAM_CHANNEL_ID",
    "@BIGBASKETDEALSINDIA"
)

API_BASE = (
    "https://api.parse.bot/scraper/"
    "1d9ca2c5-176c-4bc0-9cf3-db9056850958"
)

PRODUCT_QUERY = "Zeeba Everyday Super Mongra Basmati Rice 5 kg"


def search_bigbasket():
    url = f"{API_BASE}/search_products"

    headers = {
        "X-API-Key": PARSE_API_KEY
    }

    params = {
        "page": 1,
        "query": PRODUCT_QUERY
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=60
    )

    response.raise_for_status()

    return response.json()


def send_telegram(message):
    url = (
        f"https://api.telegram.org/"
        f"bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    )

    data = {
        "chat_id": TELEGRAM_CHANNEL_ID,
        "text": message,
        "disable_web_page_preview": False
    }

    response = requests.post(
        url,
        json=data,
        timeout=30
    )

    response.raise_for_status()


def main():
    print("Starting BigBasket price monitor...")
    print("Location: Gurgaon 122505")
    print(f"Product: {PRODUCT_QUERY}")

    data = search_bigbasket()

    print("BigBasket API response received.")

    # Print the response so we can identify
    # the exact price/product fields.
    print(json.dumps(data, indent=2)[:10000])

    print("Test completed successfully.")


if __name__ == "__main__":
    main()

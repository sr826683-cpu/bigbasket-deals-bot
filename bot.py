import os
import time
import logging
import requests

# Telegram settings
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID", "@BIGBASKETDEALSINDIA")

# Monitoring settings
CHECK_INTERVAL = 300  # 5 minutes

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def send_telegram(message):
    if not BOT_TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not configured")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

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
    return response.json()


def check_bigbasket():
    """
    BigBasket price-data source will be connected here.

    Do not scrape BigBasket directly.
    Add an authorized API/feed here when available.
    """
    logging.info("Checking BigBasket data source...")


def main():
    logging.info("BigBasket Deals Bot started")
    logging.info("Location: Gurgaon, Haryana - 122505")
    logging.info("Channel: %s", CHANNEL_ID)

    while True:
        try:
            check_bigbasket()
        except Exception as e:
            logging.error("Monitor error: %s", e)

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()

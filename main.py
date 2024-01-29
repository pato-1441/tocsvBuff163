import asyncio
import os

from dotenv import load_dotenv
from classes.BuffPricesManager import BuffPricesManager

load_dotenv(".env")
cookie_setting = os.getenv("COOKIE_SETTING")

def main():
    prices_manager = BuffPricesManager(cookie_setting)
    asyncio.run(prices_manager.run())

if __name__ == "__main__":
    main()
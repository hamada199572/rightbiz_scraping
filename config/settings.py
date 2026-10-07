# config/settings.py

import os


BASE_URL = "https://www.rightbiz.co.uk"

SEARCH_PATH = "/buy/search?location=London&search_type=restaurants"
FULL_TARGET_URL = f"{BASE_URL}{SEARCH_PATH}"

CDP_PORT = 9222
CDP_ENDPOINT = f"http://localhost:{CDP_PORT}"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "pipeline")
LOGS_DIR = os.path.join(BASE_DIR, "logger")


os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)
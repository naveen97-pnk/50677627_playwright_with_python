import os
from dotenv import load_dotenv

load_dotenv()

class Env:
    UI_BASE_URL = os.getenv("UI_BASE_URL")
    API_BASE_URL = os.getenv("API_BASE_URL")
    BROWSER = os.getenv("BROWSER")
    HEADLESS = os.getenv("HEADLESS") == "True"
    TIMEOUT = int(os.getenv("TIMEOUT", 10))
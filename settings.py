import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass
class HeadHunterSettings:
    client_id: str = os.getenv("HH_CLIENT_ID")
    client_secret: str = os.getenv("HH_CLIENT_SECRET")

@dataclass
class TelegramSettings:
    api_token: str = os.getenv("TG_TOKEN")
    chat_id: str = os.getenv("TG_CHAT_ID")

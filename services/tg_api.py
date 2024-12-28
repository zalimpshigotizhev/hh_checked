from settings import TelegramSettings
from telegram import Bot

class TelegramAPI():
    def __init__(self):
        self.settings = TelegramSettings()
        self.bot = Bot(self.settings.api_token)

    def send_message(self, message: str) -> None:
        self.bot.send_message(
            chat_id=self.settings.chat_id,
            text=message,
            parse_mode="Markdown"
        )

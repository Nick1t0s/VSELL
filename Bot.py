
from aiogram import Bot
from config import Config
print(Config.ADMINS)
bot = Bot(token=Config.BOT_TOKEN)
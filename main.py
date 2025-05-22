import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import Settings
import handlers

from Bot import bot

async def main():
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    # Регистрация обработчиков
    dp.include_router(handlers.user_handlers.router)
    dp.include_router(handlers.admin_handlers.router)

    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())

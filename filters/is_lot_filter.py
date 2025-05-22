from aiogram import types
from aiogram.filters import BaseFilter

class CreateLot(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return message.text == "Продать"
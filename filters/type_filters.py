from aiogram import types
from aiogram.filters import BaseFilter

class TextFilter(BaseFilter):
    async def __call__(self, message: types.Message):
        return message.text
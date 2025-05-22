from aiogram import types
from aiogram.filters import BaseFilter
from keyboards import KeyboardFactory

class IsType(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        if message.text in ["Под система", "Одноразка", "Жидкость", "Другое"]:
            return True
        markup = KeyboardFactory.set_type()
        await message.answer("Выберите пожалуйста из приведенного списка", reply_markup=markup)
        return False

class IsUsed(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        if message.text in ["Новое", "Б/У"]:
            return True
        markup = KeyboardFactory.get_used()
        await message.answer("Выберите пожалуйста из приведенного списка", reply_markup=markup)
        return False

class IsCost(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        print(message.text.isdigit())
        if message.text.isdigit():
            print("dfsf")
            return True
        await message.answer("Введите пожалуйста число")
        return False


from aiogram.utils.keyboard import ReplyKeyboardBuilder

def sale():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Продать")
    return builder.as_markup(resize_keyboard=True)
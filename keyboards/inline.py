from aiogram.utils.keyboard import ReplyKeyboardBuilder




class KeyboardFactory:
    @staticmethod
    def sale():
        builder = ReplyKeyboardBuilder()
        builder.button(text="Продать")
        return builder.as_markup(resize_keyboard=True)

    @staticmethod
    def set_type():
        builder = ReplyKeyboardBuilder()
        builder.button(text="Под система")
        builder.button(text="Одноразка")
        builder.button(text="Жидкость")
        builder.button(text="Другое")
        return builder.as_markup(resize_keyboard=True)

    @staticmethod
    def get_used():
        builder = ReplyKeyboardBuilder()
        builder.button(text="Новое")
        builder.button(text="Б/У")
        return builder.as_markup(resize_keyboard=True)

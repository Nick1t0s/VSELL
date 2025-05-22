from aiogram import Bot
from aiogram import types
from config import Config
from keyboards import sale
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from aiogram.types import BufferedInputFile

async def send_to_chanel(message: types.Message, state: FSMContext, bot: Bot):
    markup = sale()
    await state.update_data(text=message.caption)
    data = await state.get_data()
    await send_data_to_chanel(message=message, bot=bot, data=data)
    await message.answer("Ваш лот отправлен", reply_markup=markup)
    await state.clear()

async def send_data_to_chanel(message: types.Message,bot: Bot, data: dict):
    add_text = f"\nПо поводу покупки писать <a href='tg://user?id={message.from_user.id}'>ему</a>"
    await bot.send_photo(chat_id=Config.CHANEL,
                         photo=data["photo"],
                         caption=data["text"]+add_text,
                         parse_mode=ParseMode.HTML)

async def send_data_to_chanel_file(bot: Bot, text: str, user_id: int,photo: bytes):
    # Создаем InputFile правильно
    input_file = BufferedInputFile(photo, filename="photo.png")
    add_text = f"\nПо поводу покупки писать <a href='tg://user?id={user_id}'>ему</a>"
    await bot.send_photo(chat_id=Config.CHANEL,
                         photo=input_file,
                         caption=text+add_text,
                         parse_mode=ParseMode.HTML)

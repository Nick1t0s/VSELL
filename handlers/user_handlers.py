import asyncio

from aiogram import Router, types, Bot
from aiogram.filters import Command, StateFilter

from filters import CreateLot, TextFilter, IsUsed, IsCost, IsType
from utils import Lot, send_to_chanel
from keyboards import KeyboardFactory

from config import Config
from data.messages import Messages

from aiogram import F
from aiogram.types import Message, InputMediaPhoto
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram_media_group import media_group_handler

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    markup = KeyboardFactory.sale()
    await message.answer(
        "Привет, я бот для продажи вейпов! Для создания лота просто отправь мне Сообщение",
        reply_markup=markup
    )


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Список команд: /start, /help")


@router.message(CreateLot())
async def reg1(message: types.Message, state: FSMContext):
    markup = KeyboardFactory.set_type()
    await message.answer("Укажите тип: ", reply_markup=markup)
    await state.set_state(Lot.type)

@router.message(StateFilter(Lot.type), IsType())
async def reg2(message: types.Message, state: FSMContext):
    await state.update_data(type=message.text)
    await message.answer("Укажите модель", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(Lot.model)

@router.message(StateFilter(Lot.model), TextFilter())
async def reg3(message: types.Message, state: FSMContext):
    await state.update_data(model=message.text)
    markup = KeyboardFactory.get_used()
    await message.answer(text = "Укажите состояние товара: ", reply_markup=markup)
    await state.set_state(Lot.used)

@router.message(StateFilter(Lot.used), IsUsed())
async def reg4(message: types.Message, state: FSMContext):
    await state.update_data(used=message.text)
    await message.answer(text = "Укажите стоимость товара: ", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(Lot.cost)

@router.message(StateFilter(Lot.cost), IsCost())
async def reg5(message: types.Message, state: FSMContext):
    await state.update_data(cost=int(message.text))
    await message.answer("Укажите места, где вы можете встретиться")
    await state.set_state(Lot.place)

@router.message(StateFilter(Lot.place), TextFilter())
async def reg6(message: types.Message, state: FSMContext):
    await state.update_data(place=message.text)
    await message.answer("Укажите описание")
    await state.set_state(Lot.description)

@router.message(StateFilter(Lot.description), TextFilter())
async def reg7(message: types.Message, state: FSMContext, bot: Bot):
    await state.update_data(description=message.text)
    await message.answer("Отправьте от 1 до 3 фото")
    await state.set_state(Lot.photo)


@router.message(StateFilter(Lot.photo), F.content_type == "photo")
async def handle_photo(message: Message, state: FSMContext, bot: Bot):
    # Проверяем, есть ли media_group_id (значит это часть альбома)
    if message.media_group_id:
        # Получаем текущий список фото из состояния
        data = await state.get_data()
        album_photos = data.get("album_photos", [])

        # Добавляем текущее фото
        album_photos.append(message.photo[-1].file_id)
        await state.update_data(album_photos=album_photos)

        # Если это первое фото в альбоме - запускаем таймер обработки
        if len(album_photos) == 1:
            await asyncio.sleep(2)  # Ждем 2 секунды для сбора всех фото
            await process_album(state, bot, message)
        return
    else:
        # Одиночное фото - обрабатываем сразу
        await process_single_photo(message, state, bot)


async def process_album(state: FSMContext, bot: Bot, message: Message):
    data = await state.get_data()
    photo_ids = data.get("album_photos", [])
    if not photo_ids:
        return

    markup = KeyboardFactory.sale()
    caption = Messages.chanel_message(
        type=data["type"].replace(" ", "_"),
        model=data["model"],
        used=data["used"],
        cost=data["cost"],
        place=data["place"],
        description=data["description"],
        user_id=message.from_user.id,
    )

    # Отправляем медиагруппу
    media = [
        InputMediaPhoto(media=photo_ids[0], caption=caption, parse_mode="HTML"),
        *[InputMediaPhoto(media=photo_id) for photo_id in photo_ids[1:]],
    ]
    await bot.send_media_group(chat_id=Config.CHANEL, media=media)

    # Отправляем подтверждение
    await send_confirmation(message, bot)
    await state.clear()


async def process_single_photo(message: Message, state: FSMContext, bot: Bot):
    markup = KeyboardFactory.sale()
    data = await state.get_data()

    caption = Messages.chanel_message(
        type=data["type"].replace(" ", "_"),
        model=data["model"],
        used=data["used"],
        cost=data["cost"],
        place=data["place"],
        description=data["description"],
        user_id=message.from_user.id,
    )

    # Отправляем одиночное фото
    await bot.send_photo(
        chat_id=Config.CHANEL,
        photo=message.photo[-1].file_id,
        caption=caption,
        parse_mode="HTML",
    )

    # Отправляем подтверждение
    await send_confirmation(message, bot)
    await state.clear()


async def send_confirmation(message: Message, bot: Bot):
    markup = KeyboardFactory.sale()
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Ваш лот успешно отправлен"
    )
    await bot.send_message(
        chat_id=message.chat.id,
        text="Выберите действие:",
        reply_markup=markup
    )
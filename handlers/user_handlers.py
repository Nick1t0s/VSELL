from aiogram import Router, types, Bot, F
from aiogram.filters import Command, StateFilter
from filters.is_lot_filter import CreateLot
from aiogram.fsm.context import FSMContext
from utils import RegLot, send_to_chanel
from keyboards import sale

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    markup = sale()
    await message.answer(
        "Привет, я бот для продажи вейпов! Для создания лота просто отправь мне Сообщение",
        reply_markup=markup
    )


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Список команд: /start, /help")


@router.message(CreateLot())
async def reg1(message: types.Message, state: FSMContext):
    await state.set_state(RegLot.photo)
    await message.answer("Отправьте фото")


@router.message(F.photo, StateFilter(RegLot.photo))  # Исправлено здесь
async def reg2(message: types.Message, state: FSMContext, bot: Bot):
    await state.update_data(photo=message.photo[-1].file_id)
    print(message.caption)
    if message.caption:
        await send_to_chanel(message=message, state=state, bot=bot)
    else:
        await message.answer("Введите текст")
        await state.set_state(RegLot.text)  # Убедитесь, что у вас TEXT, а не text


@router.message(StateFilter(RegLot.text))  # Исправлено здесь
async def reg3(message: types.Message, state: FSMContext, bot: Bot):
    if not message.text:
        await message.answer("Пожалуйста, введите текст")
        return

    await send_to_chanel(message=message, state=state, bot=bot)
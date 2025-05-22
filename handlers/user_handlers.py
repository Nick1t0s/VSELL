from aiogram import Router, types, Bot
from aiogram.filters import Command, StateFilter

from filters import CreateLot, TextFilter, IsUsed, IsCost, IsType
from aiogram.fsm.context import FSMContext
from utils import Lot, send_to_chanel
from keyboards import KeyboardFactory

from config import Config
from data.messages import Messages
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

@router.message(StateFilter(Lot.place))
async def reg6(message: types.Message, state: FSMContext):
    await state.update_data(place=message.text)
    await message.answer("Укажите описание")
    await state.set_state(Lot.description)

@router.message(StateFilter(Lot.description))
async def reg7(message: types.Message, state: FSMContext, bot: Bot):
    await state.update_data(description=message.text)
    data = await state.get_data()
    print(data)
    await bot.send_message(chat_id=Config.CHANEL, text=Messages.chanel_message(
        model=data["model"],
        used=data["used"],
        cost=data["cost"],
        place=data["place"],
        description=data["description"],
        user_id=message.from_user.id
    ), parse_mode="HTML")
    await state.clear()
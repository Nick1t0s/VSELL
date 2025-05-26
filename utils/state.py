from aiogram.fsm.state import State, StatesGroup

class LotAi(StatesGroup):
    pass

class Lot(StatesGroup):
    type = State()
    model = State()
    description = State()
    used = State()
    cost = State()
    place = State()
    photo = State()
    last_media_group = State()
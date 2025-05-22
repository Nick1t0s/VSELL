from aiogram.fsm.state import State, StatesGroup

class LotAi(StatesGroup):
    pass

class Lot(StatesGroup):
    type = State()
    model = State()
    used = State()
    cost = State()
    place = State()
    description = State()


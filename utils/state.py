from aiogram.fsm.state import State, StatesGroup

class LotAi(StatesGroup):
    pass

class Lot(StatesGroup):
    model = State()
    description = State()
    used = State()
    cost = State()
    place = State()

class Pod(StatesGroup, Lot):
    condPod = State()
    condCart = State()
    color = State()

class Disp(StatesGroup, Lot):
    taste = State()
    puffs = State()

class Cart(StatesGroup, Lot):
    evap = State()
    evapR = State()
    condEvap = State()

class Evap(StatesGroup, Lot):
    evapR = State()
    condEvap = State()



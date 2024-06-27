from aiogram.fsm.state import State, StatesGroup

class States(StatesGroup):
    WELCOME = State()
    SOURCE_MANAGEMENT = State()
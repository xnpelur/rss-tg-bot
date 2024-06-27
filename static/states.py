from aiogram.fsm.state import State, StatesGroup

class States(StatesGroup):
    WELCOME = State()
    SOURCE_MANAGEMENT = State()
    ADDING_SOURCE = State()
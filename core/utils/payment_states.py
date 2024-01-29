from aiogram.fsm.state import State, StatesGroup


class TopUpCryptoBotStates(StatesGroup):
    GET_AMOUNT_CRYPTO_BOT = State()
    GET_AMOUNT_OF_PROXIES = State()
    GET_CATEGORY_OF_PROXIES = State()
    GET_GEO_OF_PROXIES = State()


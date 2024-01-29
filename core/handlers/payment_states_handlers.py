from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from core.utils.payment_states import TopUpCryptoBotStates
from aiogram import Bot
from models import order
from database.db import Db


def append_message_to_delete(message_id: int):
    from core.handlers.callbacks import messages_to_delete
    messages_to_delete.append(message_id)


async def handle_amount_value_input_for_crypto_bot(message: Message, state: FSMContext):
    await state.set_state(TopUpCryptoBotStates.GET_AMOUNT_CRYPTO_BOT)


async def get_amount_value_input_for_crypto_bot(message: Message, state: FSMContext):
    try:
        float_message = float(message.text)
        if float_message >= 3.5:
            await state.update_data(GET_AMOUNT_CRYPTO_BOT=float_message)
        else:
            await message.answer('<i>Минимальная сумма пополнения 3.5 USD.</i>')
            append_message_to_delete(message.message_id + 1)
    except ValueError as e:
        await message.answer(f'<i>Введите корректное значение суммы!</i>')
        append_message_to_delete(message.message_id + 1)


async def handle_amount_of_proxies_input(message: Message, state: FSMContext):
    await state.set_state(TopUpCryptoBotStates.GET_AMOUNT_OF_PROXIES)


async def get_amount_of_ua_proxies_input(message: Message, state: FSMContext):
    try:
        data = await state.get_data()
        category_id, geo = data.get('GET_CATEGORY_OF_PROXIES'), data.get('GET_GEO_OF_PROXIES')

        db = Db()
        amount_in_stock = await db.get_amount_of_proxies_in_stock(category_id, geo)
        int_message = int(message.text)
        user_balance = await db.get_user_balance_by_chat_id(message.from_user.id)
        proxies_amount, price = int_message, 3.5

        if 1 <= int_message <= amount_in_stock:
            order_status = order.prepare_to_checkout(user_balance, proxies_amount, amount_in_stock, price)['status']

            if order_status:
                await state.update_data(GET_AMOUNT_OF_PROXIES=int_message)
            else:
                error_message = order.prepare_to_checkout(user_balance, proxies_amount, amount_in_stock, price)[
                    "message"]
                await message.answer(f'<i>{error_message}</i>!')
                append_message_to_delete(message.message_id + 1)
    except ValueError:
        await message.answer(f'<i>Введите корректное значение количества прокси!</i>')
        append_message_to_delete(message.message_id + 1)

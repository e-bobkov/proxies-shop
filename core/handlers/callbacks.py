import time
import asyncio

from core.handlers.messages import *
from typing import Tuple
from aiogram import Bot
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto, Message
from core.keyboards.inline import *
from database.db import Db
from core.handlers.basic import *
from core.handlers.payment_states_handlers import *
from core.utils.payment_states import TopUpCryptoBotStates
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from core.settings import settings

from payments.crypto_bot.CryptoBot import CryptoBot

messages_to_delete = []


async def try_to_delete_messages(bot: Bot, call: CallbackQuery):
    try:
        await bot.delete_messages(chat_id=call.from_user.id, message_ids=messages_to_delete)
    except Exception as delete_messages_error:
        print(f"Ошибка при удалении сообщений: {delete_messages_error}")

    try:
        await call.message.delete()
    except Exception as delete_call_message_error:
        print(f"Ошибка при удалении вызывающего сообщения: {delete_call_message_error}")

    messages_to_delete.clear()


async def get_menu_inline_keyboard(call: CallbackQuery, bot: Bot):
    await try_to_delete_messages(bot, call)

    photo = InputMediaPhoto(type='photo', media=FSInputFile(MENU_PHOTO_PATH))
    await call.message.answer_media_group(media=[photo])
    messages_to_delete.append(call.message.message_id + 1)

    await call.message.answer(text=WELLCOME_TO_SHOP_MESSAGE.format(call.from_user.first_name),
                              reply_markup=menu_inline_keyboard)
    messages_to_delete.append(call.message.message_id + 2)

    await call.answer()


async def get_profile_inline_keyboard(call: CallbackQuery, bot: Bot):
    await try_to_delete_messages(bot, call)

    photo = InputMediaPhoto(type='photo', media=FSInputFile(PROFILE_PHOTO_PATH))
    await call.message.answer_media_group(media=[photo])
    messages_to_delete.append(call.message.message_id + 1)

    db = Db()
    balance = await db.get_user_balance_by_chat_id(call.from_user.id)

    await call.message.answer(text=PROFILE_MESSAGE.format(call.from_user.first_name, call.from_user.id, balance),
                              reply_markup=profile_inline_keyboard)
    messages_to_delete.append(call.message.message_id + 2)

    await call.answer()


async def get_payment_methods_inline_keyboard(call: CallbackQuery, bot: Bot):
    await try_to_delete_messages(bot, call)
    photo = InputMediaPhoto(type='photo', media=FSInputFile(TOP_UP_PHOTO_PATH))
    await call.message.answer_media_group(media=[photo])
    messages_to_delete.append(call.message.message_id + 1)
    await call.message.answer(text=PAYMENT_METHODS_MESSAGE, reply_markup=payment_methods_inline_keyboard)
    messages_to_delete.append(call.message.message_id + 2)
    await call.answer()


async def get_crypto_bot_amount_values_inline_keyboard(call: CallbackQuery, bot: Bot,
                                                       state: FSMContext):
    await try_to_delete_messages(bot, call)

    await call.message.answer(text=TOP_UP_MESSAGE, reply_markup=crypto_bot_amount_values_inline_keyboard)
    messages_to_delete.append(call.message.message_id + 1)

    await handle_amount_value_input_for_crypto_bot(call.message, state)

    while (amount := (await state.get_data()).get('GET_AMOUNT_CRYPTO_BOT')) is None or not is_valid_float(amount):
        await asyncio.sleep(2)

    crypto_bot_invoice = CryptoBot(token=settings.bots.crypto_api_key)
    invoice_id, invoice_url = await crypto_bot_invoice.create_invoice(amount=float(amount))

    await call.message.answer(text=INVOICE_CREATED_MESSAGE.format(amount),
                              reply_markup=create_inline_link(invoice_url))
    messages_to_delete.append(call.message.message_id + 2)

    is_paid = await crypto_bot_invoice.check_invoice_status(invoice_id)

    if is_paid == 'paid':

        await call.message.answer(
            text=INVOICE_WAS_PAID_MESSAGE.format(amount, amount),
            reply_markup=buy_proxies_inline_keyboard)
        messages_to_delete.append(call.message.message_id + 3)

        db = Db()
        await db.top_up_user_balance_by_chat_id(call.from_user.id, float(amount))
        await state.clear()

        await bot.send_message(settings.bots.admin_id,
                               text=ADMIN_MESSAGE_NEW_TOP_UP_MESSAGE.format(amount, call.from_user.id,
                                                                            call.from_user.username))

    else:
        await call.message.answer(text=INVOICE_UNPAID_MESSAGE.format(amount), reply_markup=go_to_menu_inline_keyboard)
        messages_to_delete.append(call.message.message_id + 3)
        await crypto_bot_invoice.delete_invoice(invoice_id)
        await state.clear()

    await call.answer()


async def get_proxy_categories_inline_keyboard(call: CallbackQuery, bot: Bot):
    await try_to_delete_messages(bot, call)
    photo = InputMediaPhoto(type='photo', media=FSInputFile(BUY_PROXIES_PHOTO_PATH))
    await call.message.answer_media_group(media=[photo])
    messages_to_delete.append(call.message.message_id + 1)
    await call.message.answer(text=CHOOSE_CATEGORY_MESSAGE, reply_markup=proxy_categories_inline_keyboard)
    messages_to_delete.append(call.message.message_id + 2)
    await call.answer()


async def get_proxy_geo_inline_keyboard(call: CallbackQuery, bot: Bot, state: FSMContext):
    await try_to_delete_messages(bot, call)
    await state.clear()
    await call.message.answer(text=CHOOSE_GEO_MESSAGE, reply_markup=proxy_geo_inline_keyboard)
    messages_to_delete.append(call.message.message_id + 1)
    await call.answer()


async def get_proxy_info(call: CallbackQuery, bot: Bot, state: FSMContext):
    await try_to_delete_messages(bot, call)

    data = DATA_MAPPING.get(call.data)

    if data:
        category_id, geo, text = data['category_id'], data['geo'], data['text']
        await state.update_data(GET_CATEGORY_OF_PROXIES=category_id)
        await state.update_data(GET_GEO_OF_PROXIES=geo)

        db = Db()
        amount_in_stock = await db.get_amount_of_proxies_in_stock(category_id, geo)
        user_balance = await db.get_user_balance_by_chat_id(call.from_user.id)

        await call.message.answer(text=text.format(user_balance, amount_in_stock),
                                  reply_markup=proxy_info_inline_keyboard)
        messages_to_delete.append(call.message.message_id + 1)

        await handle_amount_of_proxies_input(call.message, state)

        while (amount := (await state.get_data()).get('GET_AMOUNT_OF_PROXIES')) is None or not isinstance(amount, int):
            await asyncio.sleep(2)

        amount = (await state.get_data()).get('GET_AMOUNT_OF_PROXIES')
        proxies_list = await db.get_proxies_for_buyer(amount, call.from_user.id, category_id, geo)

        formatted_proxies_list = '\n\n'.join(
            [f'<code>{proxy}</code>' for proxy in proxies_list]) if proxies_list else 'No available proxies.'

        await call.message.answer(text=BUYERS_ORDER_MESSAGE.format(formatted_proxies_list),
                                  reply_markup=to_profile_inline_keyboard)
        await bot.send_message(settings.bots.admin_id,
                               text=ADMIN_MESSAGE_NEW_ORDER_MESSAGE.format(call.from_user.id, call.from_user.username,
                                                                           category_id, geo, amount, amount * 3.5))

        await db.update_user_balance_by_chat_id(call.from_user.id, amount * 3.5)
        await state.clear()

    await call.answer()


async def get_my_proxies_inline_keyboard(call: CallbackQuery, bot: Bot):
    await try_to_delete_messages(bot, call)

    photo = InputMediaPhoto(type='photo', media=FSInputFile(MY_PROXIES_PHOTO_PATH))
    await call.message.answer_media_group(media=[photo])
    messages_to_delete.append(call.message.message_id + 1)

    db = Db()
    proxies_list = await db.get_buyers_proxies(call.from_user.id)

    formatted_proxies_list = '\n\n'.join(
        [f'<code>{proxy}</code>' for proxy in proxies_list]) if proxies_list else 'No available proxies.'

    await call.message.answer(text=WELLCOME_TO_YOUR_PROXY_LIST_MESSAGE.format(formatted_proxies_list),
                              reply_markup=my_proxies_inline_keyboard)
    messages_to_delete.append(call.message.message_id + 2)

    await call.answer()


def create_inline_link(url: str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Перейти к оплате',
                url=url
            )
        ]
    ])


def is_valid_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

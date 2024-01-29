import asyncio
import logging

from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram import F
from aiogram.fsm.storage.redis import  RedisStorage

from core.settings import settings
from core.utils.commands import *
from core.handlers.callbacks import *
from core.handlers.basic import *
from core.handlers.payment_states_handlers import *



async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Bot started!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot has stopped!!')


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    storage = RedisStorage.from_url('redis://localhost:6379')

    dp = Dispatcher(storage=storage)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start, Command('start'))

    dp.callback_query.register(get_menu_inline_keyboard, F.data.startswith('go_to_menu'))

    dp.callback_query.register(get_profile_inline_keyboard, F.data.startswith('profile'))
    dp.callback_query.register(get_my_proxies_inline_keyboard, F.data.startswith('my_proxies'))
    dp.callback_query.register(get_payment_methods_inline_keyboard, F.data.startswith('top_up'))
    dp.callback_query.register(get_proxy_categories_inline_keyboard, F.data.startswith('buy_proxies'))

    dp.callback_query.register(get_proxy_geo_inline_keyboard, F.data.startswith('socks5'))
    dp.callback_query.register(get_proxy_info, F.data.startswith('ukraine'))
    dp.callback_query.register(get_proxy_info, F.data.startswith('russia'))

    dp.callback_query.register(get_crypto_bot_amount_values_inline_keyboard,
                               F.data.startswith('crypto_bot_payment_method'))

    dp.message.register(get_amount_value_input_for_crypto_bot, TopUpCryptoBotStates.GET_AMOUNT_CRYPTO_BOT)
    dp.message.register(get_amount_of_ua_proxies_input, TopUpCryptoBotStates.GET_AMOUNT_OF_PROXIES)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())

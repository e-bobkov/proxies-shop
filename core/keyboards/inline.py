from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

go_to_menu_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='📋 Меню 📋',
            callback_data='go_to_menu'
        )
    ],
])

menu_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='👤 Личный кабинет 👤',
            callback_data='profile'
        ),
    ],
    [
        InlineKeyboardButton(
            text='🧦 Мои прокси 🧦',
            callback_data='my_proxies'
        )
    ],
    [
        InlineKeyboardButton(
            text='💰 Купить прокси 💰',
            callback_data='buy_proxies'
        )
    ],
    [
        InlineKeyboardButton(
            text='💳 Пополнить баланс 💳',
            callback_data='top_up'
        )
    ],
    [
        InlineKeyboardButton(
            text='☎️ Техническая поддержка ☎️',
            url='https://t.me/midderkyc1'
        )
    ],
])

profile_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [
        InlineKeyboardButton(
            text='💳 Пополнить баланс 💳',
            callback_data='top_up'
        )
    ],
    [
        InlineKeyboardButton(
            text='🧦 Мои прокси 🧦',
            callback_data='my_proxies'
        )
    ],
    [
        InlineKeyboardButton(
            text='Назад ⬅️',
            callback_data='go_to_menu'
        )
    ],

])

my_proxies_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Назад ⬅️',
            callback_data='go_to_menu'
        )
    ],
])


crypto_bot_amount_values_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Назад ⬅️',
            callback_data='top_up'
        )
    ],
])

payment_methods_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='CryptoBot',
            callback_data='crypto_bot_payment_method'
        ),
        # InlineKeyboardButton(
        #     text='FreeKassa',
        #     callback_data='free_kassa_payment_method'
        # )
    ],
    [
        InlineKeyboardButton(
            text='Назад ⬅️',
            callback_data='go_to_menu'
        )
    ],
])

proxy_categories_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='🧦 SOCKS5 🧦',
            callback_data='socks5'
        ),
    ],
    [
        InlineKeyboardButton(
            text='Назад ⬅️',
            callback_data='go_to_menu'
        )
    ],
])

proxy_geo_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='🇷🇺 Россия 🇷🇺',
            callback_data='russia'
        ),
    ],
    [
        InlineKeyboardButton(
            text='🇺🇦 Украина 🇺🇦',
            callback_data='ukraine'
        ),
    ],
    [
        InlineKeyboardButton(
            text='Назад ⬅️',
            callback_data='buy_proxies'
        )
    ],
])

proxy_info_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Назад ⬅️',
            callback_data='socks5'
        )
    ],
])

to_profile_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='👤 Личный кабинет 👤',
            callback_data='profile'
        ),
    ],
])

buy_proxies_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='💰 Купить прокси 💰',
            callback_data='buy_proxies'
        )
    ],
])


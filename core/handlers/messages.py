WELLCOME_TO_SHOP_MESSAGE = 'Добро пожаловать в наш магазин, <i>{}</i>!'
PAYMENT_METHODS_MESSAGE = 'Выберите способ пополнения баланса:'
TOP_UP_MESSAGE = '<i>Валюта пополнения - USD.\nМинимальная сумма пополнения 3.5 USD.\n\nВведите сумму пополнения:</i>'
INVOICE_CREATED_MESSAGE = '<i>Создан счет на {} USD.\nВремя на оплату 3 минуты.</i>'
INVOICE_WAS_PAID_MESSAGE = '<i>Счет на {} USD успешно оплачен!\n\nВаш баланс пополнен на {} USD.</i>'
INVOICE_UNPAID_MESSAGE = '<i>Счет на {} USD не оплачен!</i>'
CHOOSE_CATEGORY_MESSAGE = 'Выберите категорию прокси:'
CHOOSE_GEO_MESSAGE = 'Выберите гео прокси:'
BUYERS_ORDER_MESSAGE = '<i>Ваш заказ:</i>\n\n{}'

WELLCOME_TO_YOUR_PROXY_LIST_MESSAGE = (
    'Добро пожаловать в список ваших прокси!\n\n'
    '{}'
)

PROXY_INFO_UA_MESSAGE = (
    '<i>Информация о прокси в выбранной категории:</i>\n\n'
    '🗾 Location: UA\n'
    '⚙️ Type: ISP\n'
    '⚡️ Speed: 70k-50k\n'
    '🛡 Ping: 200-300 ms\n\n'
    '<i>Срок действия 15 дней с момента покупки.</i>\n'
    '<i>Стоимость: 3.5 USD за единицу</i>\n'
    '<i>Ваш баланс: {} USD</i>\n\n'
    '<i>Минимальный заказ: 1шт.</i>\n'
    '<i>Максимальный заказ: {}шт.</i>\n\n'
    '<i>Для покупки введите желаемое количество:</i>'
)

PROXY_INFO_RU_MESSAGE = (
    '<i>Информация о прокси в выбранной категории:</i>\n\n'
    '🗾 Location: RU\n'
    '⚙️ Type: ISP\n'
    '⚡️ Speed: 60k-50k\n'
    '🛡 Ping: 150-300 ms\n\n'
    '<i>Срок действия 15 дней с момента покупки.</i>\n'
    '<i>Стоимость: 3.5 USD за единицу</i>\n'
    '<i>Ваш баланс: {} USD</i>\n\n'
    '<i>Минимальный заказ: 1шт.</i>\n'
    '<i>Максимальный заказ: {}шт.</i>\n\n'
    '<i>Для покупки введите желаемое количество:</i>'
)

PROFILE_MESSAGE = (
    '🧑 Ваш профиль\n'
    '️➖➖➖➖➖➖➖➖➖➖\n'
    '🗳 Имя: <i>{}</i>\n'
    '🆔 ID: <i>{}</i>\n\n'
    '💰 Баланс: <i>${}</i>\n\n'
    '️➖➖➖➖➖➖➖➖➖➖\n\n'
)

ADMIN_MESSAGE_NEW_TOP_UP_MESSAGE = (
    'Новое пополнение баланса\n\n'
    'На сумму {} USD\n'
    'ID: {}\n'
    'Username: @{}'
    'Сумма покупки: {} USD'
)
ADMIN_MESSAGE_NEW_ORDER_MESSAGE = (
    'Покупка в магазине\n\n'
    'ID покупателя: {}\n'
    'Username: @{}\n'
    'Категория: {}\n'
    'Гео: {}\n'
    'Количество: {}\n'
)

MENU_PHOTO_PATH = 'assets/img/menu.png'
BUY_PROXIES_PHOTO_PATH = 'assets/img/buy_proxies.png'
MY_PROXIES_PHOTO_PATH = 'assets/img/my_proxies.png'
PROFILE_PHOTO_PATH = 'assets/img/profile.png'
TOP_UP_PHOTO_PATH = 'assets/img/top_up.png'

DATA_MAPPING = {
    'ukraine': {'category_id': 'ua', 'geo': 'ua', 'text': PROXY_INFO_UA_MESSAGE},
    'russia': {'category_id': 'ru', 'geo': 'ru', 'text': PROXY_INFO_RU_MESSAGE},
}

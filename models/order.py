def order_price(proxies_amount: int, price_per_proxy: int) -> int:
    return proxies_amount * price_per_proxy


def is_enough_user_balance(user_balance: int, total_price: int) -> bool:
    return user_balance >= total_price


def is_enough_proxies_in_stock(proxies_amount: int, proxies_in_stock: int) -> bool:
    return proxies_amount <= proxies_in_stock


def prepare_to_checkout(user_balance: int, proxies_amount: int, proxies_in_stock: int, price_per_proxy: float) -> dict:
    total_price = order_price(proxies_amount, price_per_proxy)

    if not is_enough_user_balance(user_balance, total_price):
        return {
            'status': False,
            'message': 'Недостаточно средств на балансе.'
        }

    if not is_enough_proxies_in_stock(proxies_amount, proxies_in_stock):
        return {
            'status': False,
            'message': 'Недостаточно прокси в наличии'
        }

    return {
        'status': True,
        'message': 'Проверка пройдена.'
    }

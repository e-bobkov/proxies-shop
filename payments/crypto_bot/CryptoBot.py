import time
import asyncio
from typing import Tuple

from aiocryptopay import AioCryptoPay, Networks


class CryptoBot:
    def __init__(self, token: str, network: str = Networks.TEST_NET):
        self.crypto = AioCryptoPay(token=token, network=network)

    async def create_invoice(self, amount: float) -> tuple[int, str]:
        try:
            description = f'Оплата услуг в магазине @bestproxyshopbot на сумму {amount} USD'
            invoice = await self.crypto.create_invoice(amount=amount, fiat='USD', currency_type='fiat',
                                                       description=description)
            return invoice.invoice_id, invoice.bot_invoice_url
        except Exception as e:
            print(f"Ошибка при создании инвойса: {e}")

    async def check_invoice_status(self, invoice_id: int) -> str:
        start_time = time.time()
        timeout = 180  # 3 минуты
        while time.time() - start_time < timeout:
            try:
                invoices = await self.crypto.get_invoices(invoice_ids=[invoice_id], status="paid")
                if invoices and isinstance(invoices, list) and invoices[0].status == "paid":
                    print(f"Инвойс {invoice_id} оплачен")
                    return 'paid'
                else:
                    await asyncio.sleep(3)
            except Exception as e:
                print(f"Ошибка при проверке статуса инвойса: {e}")
                await asyncio.sleep(3)
        print(f"Инвойс {invoice_id} не оплачен в течение {timeout} секунд.")
        return 'unpaid'

    async def delete_invoice(self, invoice_id: int):
        try:
            success = await self.crypto.delete_invoice(invoice_id)
            if success:
                print(f"Инвойс {invoice_id} успешно удален")
            else:
                print(f"Не удалось удалить инвойс {invoice_id}")
        except Exception as e:
            print(f"Ошибка при удалении инвойса: {e}")

    async def close(self):
        await self.crypto.close()

# async def main():
#     bot = CryptoBot(token='10844:AAk5GTYuggSw5H88Pf9zdbHO9TtJaxDAvpI')
#
#     # Создание инвойса
#     # invoice_info = await bot.create_invoice(amount=1, description='Test Invoice')
#     # invoice_id, invoice_url = invoice_info
#
#     # print(f"Инвойс создан : {invoice_url}")
#     # print(f"Инвойс создан с ID: {invoice_id}")
#
#     # Проверка статуса инвойса
#     await bot.check_invoice_status('152528')
#
#     # Удаление инвойса
#     # await bot.delete_invoice(invoice_id)
#
#     # Закрытие объекта AioCryptoPay
#     await bot.close()
#
#
#
# if __name__ == '__main__':
#     import asyncio
#
#     asyncio.run(main())

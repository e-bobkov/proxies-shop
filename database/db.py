import aiosqlite

from models.user import User


class Db:
    def __init__(self, db_name='database/shop.db'):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    async def connect(self):
        self.connection = await aiosqlite.connect(self.db_name)
        self.cursor = await self.connection.cursor()

    async def close(self):
        await self.cursor.close()
        await self.connection.close()

    async def save_user(self, chat_id, username, first_name, last_name=None, balance=0):
        await self.connect()

        existing_user = await self.cursor.execute('''
            SELECT * FROM users WHERE chat_id = ?
        ''', (chat_id,))

        existing_user = await existing_user.fetchone()

        if not existing_user:
            await self.cursor.execute('''
                INSERT INTO users (chat_id, username, first_name, last_name, balance)
                VALUES (?, ?, ?, ?, ?)
            ''', (chat_id, username, first_name, last_name, balance))
            await self.connection.commit()

        await self.close()

    async def get_user_by_chat_id(self, chat_id):
        await self.connect()

        user_data = await self.cursor.execute('''
            SELECT * FROM users WHERE chat_id = ?
        ''', (chat_id,))

        user_data = await user_data.fetchone()

        if user_data:
            user_dict = {
                'chat_id': user_data[0],
                'username': user_data[1],
                'first_name': user_data[2],
                'last_name': user_data[3],
                'balance': user_data[4]
            }
            return User(**user_dict)

        await self.close()
        return None

    async def get_user_balance_by_chat_id(self, chat_id):
        await self.connect()

        user_data = await self.cursor.execute('''
            SELECT balance FROM users WHERE chat_id = ?
        ''', (chat_id,))

        user_data = await user_data.fetchone()

        if user_data:
            return user_data[0]

        await self.close()
        return None

    async def top_up_user_balance_by_chat_id(self, chat_id, amount):
        await self.connect()

        await self.cursor.execute('''
            UPDATE users SET balance = balance + ? WHERE chat_id = ?
        ''', (amount, chat_id))

        await self.connection.commit()
        await self.close()

    async def get_proxies_for_buyer(self, value, chat_id, category_id, geo, status='sold'):
        await self.connect()

        proxies = await self.cursor.execute('''
            SELECT proxy FROM proxies 
            WHERE status = 'in_stock' AND category_id = ? AND geo = ? 
            ORDER BY RANDOM() LIMIT ?
        ''', (category_id, geo, value))

        proxies = await proxies.fetchall()

        if proxies:
            await self.cursor.executemany('''
                UPDATE proxies SET status = ?, buyer_chat_id = ? WHERE proxy = ?
            ''', [(status, chat_id, proxy[0]) for proxy in proxies])

            await self.connection.commit()

            return [proxy[0] for proxy in proxies]

        await self.close()
        return None

    async def get_buyers_proxies(self, chat_id, status='sold'):
        await self.connect()

        proxies = await self.cursor.execute('''
            SELECT proxy FROM proxies WHERE buyer_chat_id = ? AND status = ?
        ''', (chat_id, status))

        proxies = await proxies.fetchall()

        if proxies:
            return [proxy[0] for proxy in proxies]

        await self.close()
        return None

    async def get_amount_of_proxies_in_stock(self, category_id, geo):
        await self.connect()

        amount = await self.cursor.execute('''
            SELECT COUNT(*) FROM proxies WHERE status = 'in_stock' AND category_id = ? AND geo = ?
        ''', (category_id, geo))

        amount = await amount.fetchone()

        await self.close()
        return amount[0]

    async def get_all_chat_ids(self):
        await self.connect()

        chat_ids = await self.cursor.execute('''
            SELECT chat_id FROM users
        ''')

        chat_ids = await chat_ids.fetchall()

        await self.close()
        return chat_ids

    async def update_user_balance_by_chat_id(self, chat_id, amount):
        await self.connect()

        await self.cursor.execute('''
            UPDATE users SET balance = balance - ? WHERE chat_id = ?
        ''', (amount, chat_id))

        await self.connection.commit()
        await self.close()







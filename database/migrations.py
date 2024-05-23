import sqlite3


def create_table_users(db_name='database/shop.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            balance INTEGER
        )
    ''')

    connection.commit()
    connection.close()


def create_table_proxies(db_name='database/shop.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS proxies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            proxy TEXT,
            category_id text,
            geo TEXT,
            price REAL,
            status TEXT,
            buyer_chat_id INTEGER
        )
    ''')

    connection.commit()
    connection.close()


def create_categories(db_name='database/shop.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id TEXT,
            category_name TEXT
        )
    ''')

    connection.commit()
    connection.close()



if __name__ == "__main__":
    create_table_users()
    create_table_proxies()
    create_categories()


import sqlite3

DB_PATH = "multiagent_memory.db"

class DBHelper:
    def __init__(self, db_path=DB_PATH):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS customers (
                                customer_id TEXT PRIMARY KEY,
                                profile TEXT
                             );''')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS products (
                                product_id TEXT PRIMARY KEY,
                                info TEXT
                             );''')

    def insert_customer(self, customer_id, profile_json):
        self.conn.execute("REPLACE INTO customers (customer_id, profile) VALUES (?, ?)", (customer_id, profile_json))
        self.conn.commit()

    def insert_product(self, product_id, info_json):
        self.conn.execute("REPLACE INTO products (product_id, info) VALUES (?, ?)", (product_id, info_json))
        self.conn.commit()

    def close(self):
        self.conn.close()

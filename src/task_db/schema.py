from .connect import Connect

def create_tables():
    conn = Connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            description TEXT NOT NULL,
            day INTEGER NOT NULL,
            time INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.disconnect()

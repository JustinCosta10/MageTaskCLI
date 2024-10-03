import sqlite3
from . import DB_NAME

class Connect:
    def __init__(self):
        self.connection = sqlite3.connect(DB_NAME)

    def cursor(self):
        if self.connection:
            return self.connection.cursor()
        else:
            raise sqlite3.ProgrammingError("Cursor access attempt failed.")

    def commit(self):
        if self.connection:
            self.connection.commit()
        else:
            raise sqlite3.ProgrammingError("Commit failed.")

    def disconnect(self):
        if self.connection:
            self.connection.close()

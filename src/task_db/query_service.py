from . import connect
from . import schema

INSERT_TASK = '''INSERT INTO tasks (description, day, time) VALUES(?,?,?)'''
DELETE_TASK = '''DELETE FROM tasks WHERE description = ?'''
SORT_TASK = '''SELECT * FROM tasks ORDER BY day ASC, time ASC'''

class QueryService:
    def __init__(self):
        try:
            self.connection = connect.Connect()
            if self.connection is None:
                raise ValueError("Failed to connect to the database")
            schema.create_tables()
        except Exception as e:
            print(f"Error: {e}")
            raise

    def __execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor

    def insert_query(self, description, day, time):
        built_params = (description, day, time)
        self.__execute_query(INSERT_TASK, built_params)
        self.connection.commit()
        print("Task inserted successfully.")

    def delete_query(self, description):
        built_param = (description,)
        self.__execute_query(DELETE_TASK, built_param)
        self.connection.commit()
        print(f"Task '{description}' deleted successfully.")

    def query_all(self):
        cursor = self.__execute_query(SORT_TASK)
        result = cursor.fetchall()
        return result

    def reset_all_tasks(self):
        """Delete all tasks to reset for a new week."""
        RESET_TASKS = 'DELETE FROM tasks'
        self.__execute_query(RESET_TASKS)
        self.connection.commit()
        print("All tasks have been reset for the new week.")

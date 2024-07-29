import sqlite3


class DBManager:
    def __init__(self, db):
        self._db = db

        self._conn = sqlite3.connect(self._db)
        self._cursor = self._conn.cursor()
        self._cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS Tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(255),
                description VARCHAR(255),
                user_id INTEGER
                );
            """
        )

    def _execute(self, query):
        self._cursor.execute(query)
        self._conn.commit()

    def add_task(self, task: dict) -> None:
        self._execute(
            f"""
            INSERT INTO Tasks(title, description, user_id)
            VALUES ('{task["title"]}', '{task["description"]}', {task['user_id']});
            """
        )

    def edit_task(self, title, new_description, user_id):
        self._execute(
            f"""
            UPDATE Tasks
            SET description='{new_description}'
            WHERE title='{title}' AND user_id={user_id};
            """
        )

    def delete_task(self, id_, user_id):
        self._execute(
            f"""
            DELETE
            FROM Tasks
            WHERE id={id_} AND user_id={user_id};
            """
        )

    def get_all_tasks(self, user_id) -> list[dict]:
        self._execute(
            f"""
            SELECT id, title, description
            FROM Tasks
            WHERE user_id={user_id};
            """
        )
        return self._cursor.fetchall()


db_manager = DBManager("database1")

import sqlite3


class DBManager:
    def __init__(self, db):
        self._db = db

        self._conn = sqlite3.connect(self._db)
        self._cursor = self._conn.cursor()
        self._cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS Tasks(
                title VARCHAR(255),
                description VARCHAR(255)
                );
            """
        )

    def _execute(self, query):
        self._cursor.execute(query)
        self._conn.commit()

    def add_task(self, task: dict) -> None:
        self._execute(
            f"""
            INSERT INTO Tasks(title, description)
            VALUES ('{task["title"]}', '{task["description"]}');
            """
        )

    def edit_task(self, title, new_description):
        self._execute(
            f"""
            UPDATE Tasks
            SET description='{new_description}'
            WHERE title='{title}';
            """
        )

    def delete_task(self, title):
        self._execute(
            f"""
            DELETE
            FROM Tasks
            WHERE title='{title}';
            """
        )

    def get_all_tasks(self) -> list[dict]:
        self._execute(
            """
            SELECT title, description
            FROM Tasks;
            """
        )
        return self._cursor.fetchall()

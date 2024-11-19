import sqlite3


class DatabaseSingleton:

    def __new__(cls, *args, **kwargs) -> "DatabaseSingleton":
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_name: str ="db.sqlite3") -> None:
        if not hasattr(self, "_instantiated"):
            self.db_name = db_name
            self.connection = sqlite3.connect(db_name)
            self.cursor = self.connection.cursor()
            self._instantiated = True


if __name__ == "__main__":
    db1 = DatabaseSingleton()
    db2 = DatabaseSingleton("fake name")
    print("Database Objects DB1", db1, db1.db_name)
    print("Database Objects DB2", db2, db2.db_name)

    db1.cursor.execute(
        "CREATE TABLE IF NOT EXISTS example_table "
        "(id INTEGER PRIMARY KEY, value TEXT)"
    )
    db1.cursor.execute(
        "INSERT INTO example_table (value) VALUES (?)", (10,)
    )
    db1.connection.commit()

    db2.cursor.execute(
        "SELECT * FROM example_table"
    )
    print("# Fetch all rows")
    rows = db2.cursor.fetchall()

    for row in rows:
        print(row)

    db1.cursor.close()
    db1.connection.close()

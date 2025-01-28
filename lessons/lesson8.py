import sqlite3

db = sqlite3.connect("UsersGrades.db")
cursor = db.cursor()


def create_tables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (20) NOT NULL,
            age INTEGER NOT NULL,
            hoby TEXT
        )
                    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades(
            gradeid INTEGER PRIMARY KEY AUTOINCREMENT<)
            userid INTEGER,
            subject VARCHAR (100) NOT NULL,
            grade INTEGER NOT NULL,
            Foreign KEY (userid) REFERENCES users(world)
        )
                    """)
    db.commit()
    print("таблицы созданы или обновлены")

create_tables()
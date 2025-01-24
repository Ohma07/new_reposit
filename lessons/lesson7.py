import sqlite3
from tkinter.font import names

#А4 бумага
db = sqlite3.connect("Users.db")
#это наша рука с ручкой
cursor = db.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            name VARCHAR (20) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT
        )
                    """)
    db.commit()

create_table()

#CRUD - создание - чтение - обновление - удаление

def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name,age,hobby)
    )
    db.commit()
    print(f"добавили {name}")
#
add_user("Олег", 22, "плавать")



def update_user_by_rowid(name=None, age=None, hobby=None, rowid=None):
    if name:
        cursor.execute(
            'UPDATE users SET name = ? WHERE rowid = ?',
            (name, rowid)
        )
    if age:
        cursor.execute(
            'UPDATE users SET age = ? WHERE rowid = ?',
            (age, rowid)
        )
    if hobby:
        cursor.execute(
            'UPDATE users SET hobby = ? WHERE rowid = ?',
            (hobby, rowid)
        )
    db.commit()
    print('Update success')

update_user_by_rowid(name="Вася Поп ит",rowid=1)

def delete_user_by_rowid(rowid):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (rowid,)
    )
    db.commit()
    print('DELETE success')

delete_user_by_rowid(1)


def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print(f"-----{users}")

    if users:
        print("Список всех пользователей")
        for user in users:
            print(f"Name: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}")
    else:
        print(f"Список пользователей пуст")

get_all_users()

db.close()
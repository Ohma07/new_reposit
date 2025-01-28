import sqlite3

# Подключение к базе данных
users_db = sqlite3.connect("Users.db")
# Курсор для выполнения SQL-запросов
cursor = users_db.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (20) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT
        )
                    """)
    users_db.commit()

create_table()

# CRUD - создание - чтение - обновление - удаление

def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    users_db.commit()
    print(f"добавили {name}")

add_user("Олег", 22, "читать")

def update_user_by_id(name=None, age=None, hobby=None, user_id=None):
    if user_id is None:
        print("Ошибка: необходимо указать корректный ID пользователя.")
        return

    cursor.execute('SELECT id FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    if not user:
        print(f"Ошибка: пользователь с ID {user_id} не найден.")
        return

    if name:
        cursor.execute('UPDATE users SET name = ? WHERE id = ?', (name, user_id))
    if age:
        cursor.execute('UPDATE users SET age = ? WHERE id = ?', (age, user_id))
    if hobby:
        cursor.execute('UPDATE users SET hobby = ? WHERE id = ?', (hobby, user_id))

    users_db.commit()
    print('Update success')

update_user_by_id(name="Вася Поп ит", user_id=1)

def delete_user_by_rowid(rowid):
    cursor.execute(
        'DELETE FROM users WHERE id = ?',
        (rowid,)
    )
    users_db.commit()
    print('DELETE success')

delete_user_by_rowid(1)

def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if users:
        print("Список всех пользователей")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, AGE: {user[2]}, HOBBY: {user[3]}")
    else:
        print("Список пользователей пуст")

get_all_users()

def detail_view_user_by_id(user_id):
    """
    Возвращает данные пользователя по его ID.
    Если пользователь не найден, возвращает сообщение об ошибке.
    """
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    if user:
        return {"id": user[0], "name": user[1], "age": user[2], "hobby": user[3]}
    else:
        return {"error": "Пользователь с данным ID не найден."}

# Пример вызова функции
user_id = int(input("Введите ID пользователя для получения информации: "))
result = detail_view_user_by_id(user_id)
print(result)

users_db.close()


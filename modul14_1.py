import sqlite3
                   # Создаем и подключаемся к базе данных
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

                    # Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
                # Заполняем таблицу Users 10 записями
# for i in range(1, 11):
#     cursor.execute("""
# INSERT INTO Users(username, email, age, balance)
# VALUES(?, ?, ?, ?)
# """,
#  (f"User{i}", f'example{i}@gmail.com', i * 10, 1000))

            # Обновляем balance у каждой 2-й записи на 500
cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")

                # Удаляем каждую 3-ю запись
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

            # Запрос на данные, где возраст не равен 60 годам
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')



connection.commit()
connection.close()
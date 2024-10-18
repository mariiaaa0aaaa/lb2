import sqlite3

# Підключення до бази даних
connection = sqlite3.connect("test.db")

# Створення курсора
cursor = connection.cursor()

# Виконання запиту для вибірки даних
cursor.execute("SELECT * FROM messages")

# Отримання результатів
rows = cursor.fetchall()

# Виведення результатів
for row in rows:
    print(row)

# Закриття з'єднання
connection.close()
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI() # ініціалізація FastAPI

# функція для підключення до бази даних SQLite
def get_db_connection():
    conn = sqlite3.connect('messages.db')
    conn.row_factory = sqlite3.Row  # для доступу до стовпців за назвою
    return conn

# функція для створення таблиці
def create_table():
    conn = get_db_connection()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS messages_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL
    )
    """)
    conn.close()

create_table() # виклик функції для створення таблиці при запуску сервера

# модель для вхідних даних
class Message(BaseModel):
    content: str

# ендпоінт для збереження даних
@app.post("/messages/")
async def create_message(message: Message):
    conn = get_db_connection()

    # вставка даних у таблицю
    try:
        conn.execute("INSERT INTO messages_table (content) VALUES (?)", (message.content,))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

    return {"messages": "Дані успішно збережено"}

# ендпоінт для отримання всіх збережених повідомлень
@app.get("/messages/")
async def read_messages():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages_table")
    rows = cursor.fetchall()

    # формування списку повідомлень
    messages = [{"id": row["id"], "content": row["content"]} for row in rows]
    conn.close()

    return {"messages": messages}
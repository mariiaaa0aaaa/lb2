from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI()

# Створення моделі для прийому даних
class Message(BaseModel):
    text: str

# Обробка POST запиту для збереження у файл
@app.post("/messages/")
async def create_message(message: Message):
    # Збереження тексту у файл
    try:
        with open("messages.txt", "a") as f:
            f.write(message.text + "\n")
        return {"message": "Дані збережено у файл"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
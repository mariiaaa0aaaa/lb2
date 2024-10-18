from fastapi import FastAPI, HTTPException
import requests
from datetime import datetime, timedelta
import uvicorn  # імпорт uvicorn для запуску сервера

app = FastAPI() # ств Flask

# функція для отримання курсу USD з нбу
def get_exchange_rate(start_date: str, end_date: str):
    url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&valcode=usd&sort=exchangedate&order=desc&json"
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Помилка при отриманні даних від НБУ.")

    return response.json()

@app.get("/currency")
async def get_currency(param: str):
    today = datetime.today()

    # визначення дати в залежності від параметра
    if param == "today":
        start_date = today.strftime('%Y%m%d')
        end_date = today.strftime('%Y%m%d')
    elif param == "yesterday":
        yesterday = today - timedelta(days=1)
        start_date = yesterday.strftime('%Y%m%d')
        end_date = yesterday.strftime('%Y%m%d')
    else:
        raise HTTPException(status_code=400, detail="Неправильний параметр. Використовуйте «today» або «yesterday».")

    # отримання даних з нбу
    exchange_data = get_exchange_rate(start_date, end_date)

    if not exchange_data:
        raise HTTPException(status_code=404, detail="На вказану дату не знайдено даних.")

    return exchange_data[0]  # повертається перший результат (найновіший курс)


# запуск сервера
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

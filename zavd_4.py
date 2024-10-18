from flask import Flask, request, jsonify, Response

app = Flask(__name__)  # ств Flask

@app.route("/data", methods=["GET"])  # визначаємо маршрут для обробки GET-запиту
def get_data():
    content_type = request.headers.get("Content-Type")  # отримуємо значення заголовка Content-Type

    # Структура відповіді
    response_data = {
        "message": "Все працює!",  # статус
        "currency": {               # дані про валюту
            "code": "USD",          # код валюти
            "rate": 41.5            # курс валюти
        }
    }

    # перевіряємо, чи заголовок Content-Type є application/json
    if content_type == "application/json":
        return jsonify(response_data)  # JSON відповідь

    # перевіряємо, чи заголовок Content-Type є application/xml
    elif content_type == "application/xml":
        # XML відповідь
        xml_data = f"""
        <response>
            <message>Все працює!</message>
            <currency>
                <code>USD</code>
                <rate>41.5</rate>
            </currency>
        </response>
        """
        return Response(xml_data, mimetype="application/xml")  # XML відповідь

    else:
        # якщо Content-Type не підходить повертаємо звичайний текст
        return "Будь ласка, встановіть правильні значення параметру заголовку “Content-Type” (application/json чи application/xml)."

if __name__ == '__main__':  # перевіряємо чи запускається файл безпосередньо
    app.run(port=8000)  # запускаємо сервер на порту 8000
from flask import Flask

app = Flask(__name__)  # ств Flask

@app.route("/")  # декоратор, який визначає маршрут для головної сторінки
def hello_world():  # функція, яка обробляє запити до маршруту "/"
    return "Веб фреймворк встановлений та веб сервер на порту 8000 запустився!"

if __name__ == '__main__':  # перевірка, чи запускається файл безпосередньо
    app.run(port=8000)  # запуск веб-сервера на порту 8000
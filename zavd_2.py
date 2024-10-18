from flask import Flask

app = Flask(__name__) # ств Flask

# лбробка GET-запиту на кореневу URL-адресу
@app.route("/", methods=["GET"])  # вказуємо, що обробляємо GET-запитом
def hello_world():
    return "Hello, World!"

if __name__ == '__main__': # перевірка, чи запускається файл безпосередньо
    app.run(port=8000)  # запуск сервера на порту 8000
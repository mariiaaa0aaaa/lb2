from flask import Flask, request

app = Flask(__name__)  # ств Flask

# обробка GET-запиту на маршруті "/currency"
@app.route("/currency", methods=["GET"])
def get_currency():
    today = request.args.get("today")  # отримуємо параметр "today" з URL

    # якщо параметр "today" передано, повертаємо курс валют
    if today is not None:  # перевіряємо, чи параметр існує
        return "USD - 41.5"  # повертаємо статичне значення курсу валют
    else:
        return "Будь ласка, вкажіть параметр 'сьогодні'."  # якщо параметр не передано

if __name__ == '__main__':  # перевірка, чи запускається файл безпосередньо
    app.run(port=8000)  # запуск сервера на порту 8000
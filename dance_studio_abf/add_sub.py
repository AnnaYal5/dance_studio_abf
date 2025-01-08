from main import app, db, Subscription

# Ініціалізація контексту додатку
with app.app_context():
    # Додавання абонементів до бази даних
    subscriptions_data = [
        {"quantity": "разове", "price": 400, "time": "місяць"},
        {"quantity": "пробне", "price": 250, "time": "місяць"},
        {"quantity": "4 тренування", "price": 1000, "time": "місяць"},
        {"quantity": "8 тренувань", "price": 1450, "time": "місяць"},
        {"quantity": "12 тренувань", "price": 1900, "time": "місяць"},
        {"quantity": "16 тренувань", "price": 2300, "time": "місяць"},
        {"quantity": "безліміт", "price": 3100, "time": "місяць"}
    ]

    # Додавання абонементів до бази даних
    for data in subscriptions_data:
        subscription = Subscription(quantity=data["quantity"], price=data["price"], time=data["time"])
        db.session.add(subscription)

    db.session.commit()

    print("Абонементи успішно додано до бази даних.")

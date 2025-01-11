from main import app, db
from models.models import Subscription
from datetime import datetime, timedelta

with app.app_context():
    # Оновлені дані підписок із часом дії
    subscriptions_data = [
        {"id": 1, "quantity": "пробне", "price": 250, "time": "30 days", "start_date": datetime.now(),
         "end_date": datetime.now() + timedelta(days=30)},
        {"id": 2, "quantity": "разове", "price": 400, "time": "30 days", "start_date": datetime.now(),
         "end_date": datetime.now() + timedelta(days=30)},
        {"id": 3, "quantity": "4 тренування", "price": 1100, "time": "30 days", "start_date": datetime.now(),
         "end_date": datetime.now() + timedelta(days=30)},
        {"id": 4, "quantity": "8 тренувань", "price": 1550, "time": "30 days", "start_date": datetime.now(),
         "end_date": datetime.now() + timedelta(days=30)},
        {"id": 5, "quantity": "'12 тренувань", "price": 1550, "time": "30 days", "start_date": datetime.now(),
         "end_date": datetime.now() + timedelta(days=30)},
        {"id": 6, "quantity": "16 тренувань", "price": 1550, "time": "30 days", "start_date": datetime.now(),
         "end_date": datetime.now() + timedelta(days=30)},
        {"id": 7, "quantity": "безліміт", "price": 1550, "time": "30 days", "start_date": datetime.now(),
         "end_date": datetime.now() + timedelta(days=30)},
    ]

    # Очищаємо таблицю підписок перед додаванням нових даних
    Subscription.query.delete()

    # Додаємо нові дані підписок
    for data in subscriptions_data:
        subscription = Subscription(
            id=data["id"],
            quantity=data["quantity"],
            price=data["price"],
            time=data["time"],
            start_date=data["start_date"],
            end_date=data["end_date"]
        )
        db.session.add(subscription)

    # Зберігаємо зміни
    db.session.commit()

    print("Підписки успішно додані до бази даних.")

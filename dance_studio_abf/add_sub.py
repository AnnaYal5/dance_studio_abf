from main import app, db
from models.models import DanceClass

with app.app_context():

    dance_classes_data = [
        {"id": 1, "direction": "Contemporary", "teacher": "Альона Мудракова", "group": "beginners 10+", "schedule": "Пн, Пт"},
        {"id": 2, "direction": "Contemporary", "teacher": "Альона Мудракова", "group": "4-8", "schedule": "Пн, Пт"},
        {"id": 3, "direction": "Contemporary", "teacher": "Юлія Грішина", "group": "middle 8-12", "schedule": "Пн, Пт"},
        {"id": 4, "direction": "Contemporary", "teacher": "Юлія Грішина", "group": "middle 14+", "schedule": "Пн, Пт"},
        {"id": 5, "direction": "Contemporary", "teacher": "Катерина Волошина", "group": "middle 13+", "schedule": "Пн, Пт"},
        {"id": 6, "direction": "Stretching", "teacher": "Альона Мудракова", "group": "all", "schedule": "Пн, Пт, Нд"},
        {"id": 7, "direction": "K-pop Dance Cover", "teacher": "Наталя Кабин", "group": "all", "schedule": "Пн, Ср, Пт, Сб"},
        {"id": 8, "direction": "Hip-Hop", "teacher": "Марія Чікнавєрова", "group": "9-12", "schedule": "Вт, Чт, Нд"},
        {"id": 9, "direction": "Hip-Hop", "teacher": "Катерина Волошина", "group": "5-7", "schedule": "Вт, Чт"},
        {"id": 10, "direction": "Hip-Hop", "teacher": "Наталя Кабин", "group": "13+", "schedule": "Ср, Сб"},
        {"id": 11, "direction": "Jazz-Funk", "teacher": "Марія Чікнавєрова", "group": "Middle 13+", "schedule": "Вт, Чт"},
        {"id": 12, "direction": "Jazz-Funk", "teacher": "Марія Чікнавєрова", "group": "Beginners 13+", "schedule": "Ср, Сб"},
        {"id": 13, "direction": "Jazz-Funk", "teacher": "Анжеліка Калюжна", "group": "Beginners 13+", "schedule": "Ср, Сб"},
        {"id": 14, "direction": "Jazz-Funk", "teacher": "Катерина Волошина", "group": "9-12", "schedule": "Вт, Чт"},
        {"id": 15, "direction": "Jazz-Funk", "teacher": "Дар’я Нечвоглод", "group": "Middle 14+", "schedule": "Вт, Чт"},
        {"id": 16, "direction": "Jazz-Funk", "teacher": "Наталя Кабин", "group": "Middle 13+", "schedule": "Ср, Сб"},
        {"id": 17, "direction": "High Heels", "teacher": "Анжеліка Калюжна", "group": "з нуля", "schedule": "Пн, Ср"},
        {"id": 18, "direction": "High Heels", "teacher": "Анжеліка Калюжна", "group": "Beginners", "schedule": "Ср, Сб"},
        {"id": 19, "direction": "High Heels", "teacher": "Дар’я Нечвоглод", "group": "PRO", "schedule": "Вт, Чт"},
        {"id": 20, "direction": "High Heels", "teacher": "Валерія Редька", "group": "Beginners", "schedule": "Вт, Чт"},
        {"id": 21, "direction": "High Heels", "teacher": "Дар’я Нечвоглод", "group": "Middle", "schedule": "Ср, Пт"},
        {"id": 22, "direction": "High Heels", "teacher": "Дарина Кулеба", "group": "Beginners", "schedule": "Ср, Сб"},
        {"id": 23, "direction": "Breakdance", "teacher": "Артем Чернокур", "group": "6+", "schedule": "Пн, Пт"}
    ]


    DanceClass.query.delete()

    for data in dance_classes_data:
        dance_class = DanceClass(
            id=data["id"],
            direction=data["direction"],
            teacher=data["teacher"],
            group=data["group"],
            schedule=data["schedule"]
        )
        db.session.add(dance_class)


    db.session.commit()

    print("Танцювальні класи успішно додані до бази даних.")


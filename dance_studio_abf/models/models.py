from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    time = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Subscription {self.quantity} - {self.price} UAH>"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscription.id'), nullable=True)
    subscription = db.relationship('Subscription', backref='user', lazy=True)



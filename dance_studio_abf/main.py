from flask import Flask, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash
import json
from config import Config
import phonenumbers
from email_validator import validate_email, EmailNotValidError
from flask_migrate import Migrate
from models.models import db, User, Subscription


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/order_subscription/<int:subscription_id>', methods=['POST'])
def order_subscription(subscription_id):
    user_id = session.get('user_id')

    if not user_id:
        flash('Потрібно зареєструватися!', 'danger')
        return redirect(url_for('register'))

    user = User.query.get(user_id)

    if user is None:
        flash('Користувача не знайдено!', 'danger')
        return redirect(url_for('index'))

    if user.subscription:
        flash('У вас вже є підписка!', 'danger')
        return redirect(url_for('user_account'))

    subscription = Subscription.query.get(subscription_id)

    if not subscription:
        flash('Підписку не знайдено!', 'danger')
        return redirect(url_for('subscriptions'))

    user.subscription = subscription
    db.session.commit()

    flash(f'Ви маєте абонемент: {subscription.quantity}', 'success')
    return redirect(url_for('user_account'))



@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('user_account'))

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']

        errors = {}

        if User.query.filter_by(email=email).first():
            errors['email'] = 'Цей email вже зареєстрований.'

        if User.query.filter_by(username=username).first():
            errors['username'] = 'Цей username вже зареєстрований.'


        try:
            parsed_number = phonenumbers.parse(phone, "UA")
            if not phonenumbers.is_valid_number(parsed_number):
                errors['phone'] = 'Недійсний номер телефону.'
        except phonenumbers.phonenumberutil.NumberParseException:
            errors['phone'] = 'Недійсний номер телефону.'


        try:
            validate_email(email)
        except EmailNotValidError as e:
            errors['email'] = str(e)

        if errors:
            return render_template('register.html', errors=errors, request=request)


        password_hash = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, email=email, password=password_hash, phone=phone)
        db.session.add(new_user)
        db.session.commit()

        session['user_id'] = new_user.id
        return redirect(url_for('user_account'))

    return render_template('register.html')


@app.route("/header")
def header():
    return render_template("header.html")


@app.route("/dance")
def dance():
    try:
        with open("dance.json", 'r', encoding='utf-8') as f:
            dance_data = json.load(f)
    except FileNotFoundError:
        flash('Dance data file not found!', 'danger')
        return redirect(url_for('index'))

    return render_template("dance.html", dance_data=dance_data)


@app.route("/subscriptions")
def subscriptions():
    subscriptions = Subscription.query.all()
    return render_template("subscriptions.html", subscriptions=subscriptions)


@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")


@app.route("/user_account")
def user_account():

    user_id = session.get('user_id')

    if not user_id:
        flash('Зареєструйтесь!', 'danger')
        return redirect(url_for('register'))


    user = User.query.get(user_id)

    if user is None:
        flash('Користувача не знайдено!', 'danger')
        return redirect(url_for('index'))

    return render_template("user_account.html", user=user)


@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

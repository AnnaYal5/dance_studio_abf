from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import json

app = Flask(__name__)
app.secret_key = "fjyhcvhtfd5667bl"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(13), nullable=False)

@app.route('/register', methods=['GET', 'POST'])
def register():

    if 'user_id' in session:
        flash('You are already logged in.', 'info')
        return redirect(url_for('user_account'))

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('User already exists!', 'danger')
            return redirect(url_for('register'))

        password_hash = generate_password_hash(password, method='pbkdf2:sha256')

        new_user = User(username=username, email=email, password=password_hash, phone=phone)
        db.session.add(new_user)
        db.session.commit()


        session['user_id'] = new_user.id
        flash('Registration successful! You are now logged in.', 'success')
        return redirect(url_for('user_account'))

    return render_template('register.html')

@app.route("/header")
def header():
    return render_template("header.html")

@app.route("/dance")
def dance():
    # Load the JSON data from the file
    try:
        with open("dance.json", 'r', encoding='utf-8') as f:
            dance_data = json.load(f)
    except FileNotFoundError:
        flash('Dance data file not found!', 'danger')
        return redirect(url_for('index'))

    # Pass the data to the template
    return render_template("dance.html", dance_data=dance_data)

@app.route("/ticket")
def ticket():
    return render_template("ticket.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/user_account")
def user_account():

    user_id = session.get('user_id')

    if not user_id:
        flash('You must be logged in to view your account!', 'danger')
        return redirect(url_for('register'))


    user = User.query.get(user_id)

    if user is None:
        flash('User not found!', 'danger')
        return redirect(url_for('index'))

    return render_template("user_account.html", user=user)

@app.route("/logout")
def logout():
    session.pop('user_id', None)  # Видаляємо id користувача з сесії
    flash('You have been logged out!', 'info')
    return redirect(url_for('index'))

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

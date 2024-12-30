from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

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

        flash('Registration successful! Please select a membership plan.', 'success')
        return redirect(url_for('user_account'))

    return render_template('register.html')


with app.app_context():
    db.create_all()
@app.route("/header")
def header():
    return render_template("header.html")

@app.route("/dance")
def dance():
    return render_template("dance.html")

@app.route("/ticket")
def ticket():
    return render_template("ticket.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/user_account/<int:user_id>")
def user_account(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("user_account.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)

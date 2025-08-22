from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from models import User, Prediction
import numpy as np
import pickle
import os
from dotenv import load_dotenv
from email_validator import validate_email, EmailNotValidError

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
model = pickle.load(open("hdp_model.pkl", "rb"))

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Initialize Bcrypt
bcrypt = Bcrypt(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Validate email
        try:
            validate_email(email)
        except EmailNotValidError:
            flash('Invalid email address', 'error')
            return redirect(url_for('register'))

        # Validate password
        if len(password) < 8:
            flash('Password must be at least 8 characters long', 'error')
            return redirect(url_for('register'))
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('register'))

        # Check if user already exists
        if User.get_by_email(email):
            flash('Email already registered', 'error')
            return redirect(url_for('register'))

        # Create new user
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User.create(name, email, hashed_password)
        login_user(user)
        return redirect(url_for('sub'))

    return render_template("register.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.get_by_email(email)

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('sub'))
        else:
            flash('Invalid email or password', 'error')
            return redirect(url_for('login'))

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/profile")
@login_required
def profile():
    predictions = Prediction.get_user_predictions(current_user.id)
    return render_template("profile.html", user=current_user, predictions=predictions)

@app.route("/delete_prediction/<prediction_id>", methods=['POST'])
@login_required
def delete_prediction(prediction_id):
    Prediction.delete_prediction(prediction_id, current_user.id)
    return redirect(url_for('profile'))

@app.route("/sub")
@login_required
def sub():
    return render_template("sub.html")

# @app.route("/hdy", methods=["POST"])
# @login_required
# def hdy():
#     return render_template("hdy.html")

# @app.route("/hdn", methods=["POST"])
# @login_required
# def hdn():
#     return render_template("hdn.html")

@app.route("/predict", methods=["POST"])
@login_required
def predict():
    if request.method == "POST":
        input_data = {
            'age': int(request.form["age"]),
            'sex': int(request.form["sex"]),
            'cp': int(request.form["cp"]),
            'trestbps': int(request.form["trestbps"]),
            'chol': int(request.form["chol"]),
            'fbs': int(request.form["fbs"]),
            'restecg': int(request.form["restecg"]),
            'thalach': int(request.form["thalach"]),
            'exang': int(request.form["exang"]),
            'oldpeak': float(request.form["oldpeak"]),
            'slope': int(request.form["slope"]),
            'ca': int(request.form["ca"]),
            'thal': int(request.form["thal"])
        }

        values = np.array([list(input_data.values())])
        prediction = model.predict(values)[0]

        # Save prediction to database
        Prediction.create(current_user.id, input_data, int(prediction))

        return render_template("predict.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True) 

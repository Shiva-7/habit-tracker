from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Secret key for session management
    app.config['SECRET_KEY'] = 'your_secret_key_here'

    # SQLite database (for simplicity, later we can move to AWS RDS)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/users.db'
    db.init_app(app)

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)

    from .models import User
    with app.app_context():
        db.create_all()  # Creates tables if they don't exist

    return app

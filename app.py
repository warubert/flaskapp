from flask import Flask, flash, jsonify, redirect, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'
    app.secret_key = 'your_secret_key'
    
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.init_app(app)

    from models import User
    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)
    
    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect(url_for('index'))

    bcrypt = Bcrypt(app)

    migrate = Migrate(app, db)

    from routes import register_routes
    register_routes(app, db, bcrypt)
    
    return app

flask_app = create_app()
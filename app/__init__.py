from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .config import Config
from flask_socketio import SocketIO

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    

    from app.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    from app.routes import main as main_blueprint
    # app.register_blueprint(main_blueprint)
    app.register_blueprint(main_blueprint, url_prefix='/')
    return app
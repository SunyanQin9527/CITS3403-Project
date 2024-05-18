from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .config import Config
#重置密码
from flask_mail import Mail




db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
#重置密码
mail = Mail()





def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)


    #重置密码
    mail.init_app(app)


    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    from app.routes import main as main_blueprint
    # app.register_blueprint(main_blueprint)
    app.register_blueprint(main_blueprint, url_prefix='/')

    return app

from app import models
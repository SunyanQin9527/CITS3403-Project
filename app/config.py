import os



basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "2b_is_great"
    #重置密码
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'cits3403groupproject0309@gmail.com'  # 在环境变量中设置
    MAIL_PASSWORD = 'xzqytcwiajplxlsj'  # 在环境变量中设置
    MAIL_DEFAULT_SENDER = 'cits3403groupproject0309@gmail.com'  # 发件人信息

from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date
from sqlalchemy.orm import relationship

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    profile_image = db.Column(db.String(120), default='default.jpg')
    joined_at = db.Column(db.DateTime, default=datetime.now)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    threads_created = db.Column(db.Integer, default=0)
    likes_received = db.Column(db.Integer, default=0)
    credit_points = db.Column(db.Integer, default=0)
    avatar = db.Column(db.String(128), default='/static/profile-pictures/default_avatar.png')
    about_me = db.Column(db.String(500), default='')  # 新增字段
    age = db.Column(db.String(120), default='Please set your age')  # 修改类型为字符串以存储默认消息
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)

    def get_id(self):
        return self.user_id


class Post(db.Model):
    __tablename__ = 'post'  # 明确指定表名
    post_id = db.Column(db.String(8), primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
    user_id = db.Column(db.String(8), db.ForeignKey('user.user_id'))  # 修改外键关系
    answers = db.relationship('Answer', backref='question', lazy='dynamic')

class Answer(db.Model):
    __tablename__ = 'answer'  # 明确指定表名
    answer_id = db.Column(db.String(8), primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
    user_id = db.Column(db.String(8), db.ForeignKey('user.user_id'))  # 修改外键关系
    post_id = db.Column(db.String(8), db.ForeignKey('post.post_id'))  # 修改外键关系

class Avatar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), unique=True)
    path = db.Column(db.String(255), unique=True)

    def __repr__(self):
        return '<Avatar filename={}>'.format(self.filename)




class CheckIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    checkin_date = db.Column(db.Date, default=date.today)
    user = relationship('User', backref='checkins')

    @staticmethod
    def has_checked_in_today(user_id):
        return CheckIn.query.filter_by(user_id=user_id, checkin_date=date.today()).first() is not None

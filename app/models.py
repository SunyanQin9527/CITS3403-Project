from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

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

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)

    def get_id(self):
        return self.user_id


class Post(db.Model):
    __tablename__ = 'post'  # 明确指定表名
    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 确保设置为自动增长
    title = db.Column(db.String(140))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))  # 修改外键关系
    answers = db.relationship('Answer', backref='question', lazy='dynamic')

    answers = db.relationship('Answer', backref='post', lazy='dynamic')

class Answer(db.Model):
    __tablename__ = 'answer'  # 明确指定表名
    answer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 使用自增的整数主键
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))  # 确保外键类型一致
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'))  # 修改外键关系



from sqlalchemy import func
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date
from sqlalchemy.orm import relationship

#重置密码工具
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer  # 修改这一行

from flask import current_app

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    profile_image = db.Column(db.String(120), default='default.jpg')
    joined_at = db.Column(db.DateTime, default=datetime.now)
    threads_created = db.Column(db.Integer, default=0)
    likes_received = db.Column(db.Integer, default=0)
    credit_points = db.Column(db.Integer, default=0)
    avatar = db.Column(db.String(128), default='/static/profile-pictures/default_avatar.png')
    about_me = db.Column(db.String(500), default='')
    age = db.Column(db.String(120), default='Please set your age')
    
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    answers = db.relationship('Answer', backref='author', lazy='dynamic')
    sent_messages = db.relationship('Message', foreign_keys='Message.sender_id', backref='sender', lazy='dynamic')
    received_messages = db.relationship('Message', foreign_keys='Message.recipient_id', backref='recipient', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.user_id

    def __repr__(self):
        return f'<User {self.username}>'


     #发邮件重置密码
    def get_reset_password_token(self, expires_in=600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in)
        return s.dumps({'reset_password': self.user_id}).decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['reset_password'])


class Post(db.Model):
    __tablename__ = 'post'
    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(140))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    answers = db.relationship('Answer', backref='post', lazy='dynamic')

    def __repr__(self):
        return f'<Post {self.title}>'


class Answer(db.Model):
    __tablename__ = 'answer'
    answer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'))

    def __repr__(self):
        return f'<Answer {self.body[:20]}>'


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


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Message {self.body[:20]}>'
from sqlalchemy import func
from app import db,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
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
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    threads_created = db.Column(db.Integer, default=0)
    likes_received = db.Column(db.Integer, default=0)
    credit_points = db.Column(db.Integer, default=0)
    answers = relationship('Answer', back_populates='author')

    member_since = db.Column(db.DateTime, default=func.now())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)

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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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
    author = relationship('User', back_populates="answers")


    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))  # 确保外键类型一致
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'))  # 修改外键关系


#发送信息
class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    sender = db.relationship('User', foreign_keys=[sender_id], backref='sent_messages')
    recipient = db.relationship('User', foreign_keys=[recipient_id], backref='received_messages')




from faker import Faker
from your_application import db
from your_application.models import User, Post, Answer, Avatar, CheckIn, FriendRequest, Product
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta, date
import random

fake = Faker()

def create_users(num_users=100):
    for _ in range(num_users):
        user = User(
            username=fake.unique.user_name(),
            email=fake.unique.email(),
            password_hash=generate_password_hash('defaultpassword'),
            profile_image='default.jpg',
            joined_at=fake.past_date(),
            threads_created=random.randint(0, 100),
            likes_received=random.randint(0, 500),
            credit_points=random.randint(0, 1000),
            avatar='/static/profile-pictures/default_avatar.png',
            about_me=fake.text(),
            age=str(fake.random_int(min=18, max=80))
        )
        db.session.add(user)
    db.session.commit()

def create_posts(num_posts=200):
    user_ids = [user.user_id for user in User.query.all()]
    for _ in range(num_posts):
        post = Post(
            title=fake.sentence(),
            body=fake.text(),
            timestamp=fake.past_datetime(),
            user_id=random.choice(user_ids)
        )
        db.session.add(post)
    db.session.commit()

def create_answers(num_answers=500):
    post_ids = [post.post_id for post in Post.query.all()]
    user_ids = [user.user_id for user in User.query.all()]
    for _ in range(num_answers):
        answer = Answer(
            body=fake.paragraph(),
            timestamp=fake.past_datetime(),
            user_id=random.choice(user_ids),
            post_id=random.choice(post_ids)
        )
        db.session.add(answer)
    db.session.commit()

def create_products(num_products=50):
    for _ in range(num_products):
        product = Product(
            name=fake.word(),
            image_url=fake.image_url(),
            price=random.randint(100, 1000)
        )
        db.session.add(product)
    db.session.commit()

# 调用这些函数来生成数据
create_users()
create_posts()
create_answers()
create_products()

print("Data generation complete!")

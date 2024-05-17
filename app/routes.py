
from urllib.parse import urlparse
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required

from app import db
from app.models import User,Avatar
from app.forms import RegistrationForm, LoginForm

main = Blueprint('main', __name__)

@main.route('/')

@main.route('/homepage')
def homepage():
    return render_template('homepage.html', title='Homepage')


@main.route('/shop')
@login_required
def shop():
    return render_template('shop.html')



@main.route('/forum')
@login_required
def forum():
    return render_template('forum.html', title='Forum')

@main.route('/chat')
@login_required
def chat():
    return render_template('chat.html')

@main.route('/profile')
@login_required
def profile():
    user = {"ID": "12345", "Age": "30", "posts": 10, "threads_created": 5, "likes_received": 15, "credit_points": 100}
    avatars = Avatar.query.all()  # 确保这一行正确无误
    print(avatars)
    return render_template('profile.html', user=current_user, avatars=avatars)

# 头像
@main.route('/update-avatar', methods=['POST'])
def update_avatar():
    
    if not current_user.is_authenticated:
        return redirect(url_for('main.login'))

    avatar_url = request.form['avatar']
    if avatar_url:
        current_user.avatar = avatar_url
        db.session.commit()
        flash(f'Your avatar has been updated.', 'success')
        print(f'Updated avatar URLllllllllls: {current_user.avatar}') 
    else:
        flash(f'Please select an avatar.', 'error')
    
    return redirect(url_for('main.profile'))

@main.route('/contact')
@login_required
def contact():
    return render_template('contact.html', title='Contact')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.homepage'))  # 修改重定向目标为 'main.homepage'
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()


        if user is None:
            flash(f'Email address not found', 'error')
            return redirect(url_for('main.login'))
        
        if not user.check_password(form.password.data):
            flash(f'Incorrect password', 'error')
            return redirect(url_for('main.login'))

        login_user(user, remember=True)
        next_page = request.args.get('next')
        
        # Check if the next_page is safe
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('main.homepage')
        
        return redirect(next_page)
        
    return render_template('login.html', title='Sign In', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.homepage'))



@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated and not request.args.get('force'):
        return redirect(url_for('main.homepage'))
    form = RegistrationForm()


    error_messages = []  # 创建一个列表来收集错误消息

    if form.validate_on_submit():
        
        # 检查用户名是否已存在
        if User.query.filter_by(username=form.username.data).first():
            
            error_messages.append('Username already exists')

        # 检查邮箱是否已被注册
        if User.query.filter_by(email=form.email.data).first():
            error_messages.append('Email already registered')

        # 验证两次密码是否一致
        if form.password.data != form.confirm_password.data:
            error_messages.append('Passwords do not match')

        # 验证密码长度
        if len(form.password.data) < 5:
            error_messages.append('Password must be at least 5 characters long')

        # 如果有错误消息，flash它们，然后重定向到注册页面
        if error_messages:
            for message in error_messages:
                flash(f'{message}', 'error')
            return redirect(url_for('main.register'))

        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        
        flash(f'Congratulations, you are now a registered user!', 'success')  # 修改为'success'
        return redirect(url_for('main.login'))

        
    return render_template('register.html', title='Register', form=form)




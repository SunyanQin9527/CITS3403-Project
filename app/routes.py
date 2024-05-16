# from flask import Flask,render_template, redirect, url_for, flash, request
# from flask_login import login_user, login_required, logout_user, current_user
# from app import create_app, flaskApp, db
# from app.models import User
# from app.forms import LoginForm, RegistrationForm, PasswordResetForm
# from werkzeug.security import generate_password_hash, check_password_hash

# app = create_app()

# @flaskApp.route("/")
# def homepage():
#         return render_template('homepage.html')

# @flaskApp.route('/forum')
# def forum():
#     return render_template('forum.html')

# @flaskApp.route('/profile')
# def profile():
#     user = {"ID": "12345", "Age": "30", "posts": 10, "threads_created": 5, "likes_received": 15, "credit_points": 100}
#     return render_template('profile.html', user=user)

# @flaskApp.route('/contact')
# def contact():
#     return render_template('contact.html')

# @flaskApp.route('/chat')
# def chat():
#     return render_template('chat.html')

# @flaskApp.route('/shop')
# def shop():
#     return render_template('shop.html')

# @flaskApp.route('/logn-signup')
# def login_button():
#     return render_template('homepage.html')

# #临时文件
# @flaskApp.route('/show_users')
# def show_users():
#     users = User.query.all()
#     return '<br>'.join([f'{user.email}: {user.password_hash}' for user in users])


# #临时文件




# @flaskApp.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and user.check_password(form.password.data):
#             login_user(user)
#             flash('You have been successfully logged in.', 'success')
#             return redirect(url_for('profile'))  # Redirect to the profile page
#         else:
#             flash('Invalid email or password.', 'danger')
#     return render_template('login.html', form=form)

# @flaskApp.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(email=form.email.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Your account has been created! You are now able to log in.', 'success')
#         return redirect(url_for('login'))
#     return render_template('register.html', form=form)

# @flaskApp.route('/reset_password', methods=['GET', 'POST'])
# def reset_password():
#     form = PasswordResetForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user:
#             # TODO: Implement password reset email sending logic
#             flash('A password reset link has been sent to your email.', 'info')
#         else:
#             flash('Email not found.', 'warning')
#     return render_template('reset_password.html', form=form)

# @flaskApp.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('You have been logged out.', 'info')
#     return redirect(url_for('homepage'))
# @app.route('/index')
# @login_required
# def index():
#     return render_template('index.html', title='Home')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid email or password')
#             return redirect(url_for('login'))
#         login_user(user, remember=True)
#         next_page = request.args.get('next')
#         if not next_page or url_parse(next_page).netloc != '':
#             next_page = url_for('index')
#         return redirect(next_page)
#     return render_template('login.html', title='Sign In', form=form)

# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Congratulations, you are now a registered user!')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import db
from app.models import User
from app.forms import RegistrationForm, LoginForm

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')

@main.route('/shop')
@login_required
def shop():
    return render_template('shop.html')

@main.route('/homepage')
@login_required
def homepage():
    return render_template('homepage.html', title='Homepage')

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
    return render_template('profile.html', user=user)

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
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('main.login'))
        login_user(user, remember=True)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.homepage')  # 修改重定向目标为 'main.homepage'
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated and not request.args.get('force'):
        return redirect(url_for('main.homepage'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)


##下面是创建帖子

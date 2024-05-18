
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
# from werkzeug.urls import url_parse
from app import db,mail
# from urllib.parse import urlparse

from app.forms import RegistrationForm, LoginForm
from app.models import User,Post, Answer,Message
#重置密码

from app.forms import  ResetPasswordForm
from flask import current_app as app
from flask_mail import Message
from app.forms import RegistrationForm, LoginForm, RequestResetForm
from app.email import send_password_reset_email 


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
def forum():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('forum.html', posts=posts)


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

@main.route('/question/<int:question_id>')
def view_question(question_id):
    question = Post.query.get_or_404(question_id)  # 获取问题或者返回404错误
    return render_template('question_detail.html', question=question)


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
@main.route('/submit-question', methods=['POST'])
def submit_question():
    if not current_user.is_authenticated:
        return redirect(url_for('main.login'))
    
    title = request.form['forumtitle']
    body = request.form['discussionQuestion']
    new_post = Post(title=title, body=body, user_id=current_user.user_id)
    db.session.add(new_post)
    db.session.commit()
    flash('Your question has been posted.')
    return redirect(url_for('main.forum'))

@main.route('/submit-answer/<int:post_id>', methods=['POST'])
def submit_answer(post_id):
    if not current_user.is_authenticated:
        return redirect(url_for('main.login'))
    
    body = request.form['answerContent']
    new_answer = Answer(body=body, post_id=post_id, user_id=current_user.user_id)
    db.session.add(new_answer)
    db.session.commit()
    flash('Your answer has been posted.')
    return redirect(url_for('main.forum'))


#接下来是发送信息和查看用户

@main.route('/send-message/<int:recipient_id>', methods=['POST'])
def send_message(recipient_id):
    if not current_user.is_authenticated:
        return redirect(url_for('main.login'))
    
    recipient = User.query.get_or_404(recipient_id)
    body = request.form['message']
    new_message = Message(sender_id=current_user.user_id, recipient_id=recipient_id, body=body)
    db.session.add(new_message)
    db.session.commit()
    flash(f'Your message has been sent to {recipient.username}.')
    return redirect(url_for('main.view_user', user_id=recipient_id))

@main.route('/user/<int:user_id>')
def view_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_profile.html', user=user)


#下面是搜索功能
@main.route('/search')
def search():
    query = request.args.get('search')
    if query:
        posts = Post.query.filter(Post.title.contains(query) | Post.body.contains(query)).all()
    else:
        posts = Post.query.all()
    return render_template('forum.html', posts=posts)

#下面是删除帖子
@main.route('/delete-question/<int:question_id>', methods=['POST'])
@login_required
def delete_question(question_id):
    question = Post.query.get_or_404(question_id)
    if question.user_id != current_user.user_id:
        flash('You do not have permission to delete this question.')
        return redirect(url_for('main.forum'))
    db.session.delete(question)
    db.session.commit()
    flash('Your question has been deleted.')
    return redirect(url_for('main.forum'))

#下面是重置密码
@main.route('/reset_password_request', methods=['GET', 'POST'])
def request_password_reset():
    if current_user.is_authenticated:
        return redirect(url_for('main.homepage'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('main.login'))
    return render_template('reset_password_request.html', title='Reset Password', form=form)

@main.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.homepage'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('main.homepage'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.', 'success')
        return redirect(url_for('main.login'))
    return render_template('reset_password.html', form=form)

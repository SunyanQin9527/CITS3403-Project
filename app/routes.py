from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from flask_login import current_user, login_user, logout_user, login_required

from app import db, mail
# from urllib.parse import urlparse

from app.forms import RegistrationForm, LoginForm, EditProfileForm
from app.models import User, Post, Answer, Avatar, CheckIn, Message,Product



from app.forms import  ResetPasswordForm
from flask import current_app as app
from flask_mail import Message
from app.forms import RegistrationForm, LoginForm, RequestResetForm
from app.email import send_password_reset_email 

from app.models import User




main = Blueprint('main', __name__)

@main.route('/')



@main.route('/homepage')

def homepage():
    return render_template('homepage.html', title='Homepage')



@main.route('/forum', methods=['GET'])
@login_required
def forum():
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('search', '')
    theme = request.args.get('theme', 'light')

    if search_query:
        posts = Post.query.filter(Post.title.contains(search_query)).order_by(Post.timestamp.desc()).paginate(page=page, per_page=3)
    else:
        posts = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=3)

    return render_template('forum.html', posts=posts, search_query=search_query, theme=theme)



@main.route('/shop')
@login_required
def shop():
    products = Product.query.all()
    return render_template('shop.html',products=products)

@main.route('/buy-product', methods=['POST'])
@login_required
def buy_product():
    product_id = request.form.get('product_id')
    product = Product.query.get(product_id)
    
    if not product:
        flash(f"Product not found.", "error")
        return redirect(url_for('main.shop'))

    if current_user.credit_points >= product.price:
        current_user.credit_points -= product.price
        current_user.avatar = product.image_url  
        db.session.commit()
        flash(f"Purchase successful! Product image now available as an avatar option.", "success")
    else:
        flash(f"You do not have enough credit_points to buy this product.", "error")

    return redirect(url_for('main.shop'))


@main.route('/chat')
@login_required
def chat():
    return render_template('chat.html')





@main.route('/search_user', methods=['POST'])
def search_user():
    search_term = request.form['searchTerm']
    users = User.query.filter((User.username.like(f'%{search_term}%')) | (User.email.like(f'%{search_term}%'))).all()
    return render_template('search_results.html', users=users)

@main.route('/add_friend', methods=['POST'])
@login_required
def add_friend():
    user_id = request.form['userId']
    if user_id and user_id.isdigit():
        new_friend = FriendRequest(from_user_id=current_user.user_id, to_user_id=int(user_id))
        db.session.add(new_friend)
        db.session.commit()
        return jsonify({'message': 'Friend request sent', 'status': 'success'})
    else:
        return jsonify({'message': 'Invalid user ID', 'status': 'error'})


@main.route('/profile')
@login_required
def profile():
    user = {
        "ID": current_user.user_id,
        "Age": current_user.age if current_user.age else 'Please set your age',
        "posts": current_user.posts.count(),  
        "threads_created": current_user.threads_created,
        "likes_received": current_user.likes_received,
        "credit_points": current_user.credit_points
    }
    avatars = Avatar.query.all() 
    has_checked_in_today = CheckIn.has_checked_in_today(current_user.user_id)
    print(avatars)
    return render_template('profile.html', user=user, avatars=avatars,has_checked_in_today=has_checked_in_today)




# Avatars
@main.route('/update-avatar', methods=['POST'])
def update_avatar():
    
    if not current_user.is_authenticated:
        return redirect(url_for('main.login'))

    avatar_url = request.form['avatar']
    if avatar_url:
        current_user.avatar = avatar_url
        db.session.commit()
        flash(f'Your avatar has been updated.', 'success')
        
    else:
        flash(f'Please select an avatar.', 'error')
    
    return redirect(url_for('main.profile'))








@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(obj=current_user) 
    if request.method == 'POST':
        about_me = request.form['about_me']
        current_user.about_me = about_me
        current_user.age = form.age.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.age.data = current_user.age
    return render_template('edit-profile.html', form=form)





@main.route('/check-in', methods=['POST'])
@login_required
def check_in():
    if CheckIn.has_checked_in_today(current_user.user_id):
        flash('You have already checked in today.')
    else:
        new_checkin = CheckIn(user_id=current_user.user_id)
        current_user.credit_points += 200  
        db.session.add(new_checkin)
        db.session.commit()
        flash('Check-in successful! You earned 200 credit points.')
    return redirect(url_for('main.profile'))









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





@main.route('/contact')
@login_required
def contact():
    return render_template('contact.html', title='Contact')





@main.route('/question/<int:question_id>')
def view_question(question_id):
    question = Post.query.get_or_404(question_id)  
    return render_template('question_detail.html', question=question)






@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.homepage'))  
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


    error_messages = [] 

    if form.validate_on_submit():
        

        if User.query.filter_by(username=form.username.data).first():
            
            error_messages.append('Username already exists')


        if User.query.filter_by(email=form.email.data).first():
            error_messages.append('Email already registered')


        if form.password.data != form.confirm_password.data:
            error_messages.append('Passwords do not match')


        if len(form.password.data) < 5:
            error_messages.append('Password must be at least 5 characters long')


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
    return render_template('reset_password2.html', form=form)





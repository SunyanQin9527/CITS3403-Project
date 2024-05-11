from flask import  render_template
from app import flaskApp


@flaskApp.route("/")
def homepage():
        return render_template('homepage.html')

@flaskApp.route('/forum')
def forum():
    return render_template('forum.html')

@flaskApp.route('/profile')
def profile():
    user = {"ID": "12345", "Age": "30", "posts": 10, "threads_created": 5, "likes_received": 15, "credit_points": 100}
    return render_template('profile.html', user=user)

@flaskApp.route('/contact')
def contact():
    return render_template('contact.html')

@flaskApp.route('/chat')
def chat():
    return render_template('chat.html')

@flaskApp.route('/shop')
def shop():
    return render_template('shop.html')
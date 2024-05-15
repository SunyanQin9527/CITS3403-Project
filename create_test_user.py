from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()
app.app_context().push()

def create_test_users():
    users = [
        {"email": "test1@example.com", "password": "password123"},
        {"email": "test2@example.com", "password": "password123"},
        {"email": "test3@example.com", "password": "password123"},
    ]

    for user in users:
        hashed_password = generate_password_hash(user['password'], method='sha256')
        new_user = User(email=user['email'], password_hash=hashed_password)
        db.session.add(new_user)
    
    db.session.commit()
    print("Test users created.")

if __name__ == '__main__':
    create_test_users()

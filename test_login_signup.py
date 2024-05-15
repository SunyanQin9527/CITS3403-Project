import requests

BASE_URL = "http://localhost:5000"

def test_signup():
    signup_url = f"{BASE_URL}/register"
    data = {
        "email": "testsignup@example.com",
        "password": "password123",
        "confirm_password": "password123"
    }
    response = requests.post(signup_url, data=data)
    print("Signup Response:", response.text)

def test_login():
    login_url = f"{BASE_URL}/login"
    data = {
        "email": "test1@example.com",
        "password": "password123"
    }
    response = requests.post(login_url, data=data)
    print("Login Response:", response.text)

if __name__ == '__main__':
    test_signup()
    test_login()

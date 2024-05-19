## Authors

- Pengyu Lu  - 23201541
- Sunayn Qin - 23208949
- Leyi Chen - 23442577
- Bowen Guo - 23152491

## Design

### Login & signup page
- An incorrect user name or password will be displayed.
- Username or email already exists will be displayed.
- Password must be at least 5 characters long.

### Navigation Bar Design
- Position: Top of the page.
- Content: Includes links like Home, Forum, Profile, Contact, etc.
- Function: Provides users with quick navigation to different pages.

### Homepage Design
- Title: Displays the website name and tagline in large font.
- Color: The title uses a rainbow gradient to attract attention.
- Introductory Text: Briefly introduces the website's features, using colors consistent with the overall design.

### Forum Page Design
- Form: Includes input fields for discussion title, question content, and reward points.
- Button: Green "Post Question" button that stands out and is easy to click.
- Question List: Shows existing discussion topics, ordered by posting time.
- Pagination Controls: Pagination navigation at the bottom to help users browse more content.

### User Profile Page Design
- Profile: When registered, users will have a default avatar, and 12 free avatars, which users can choose according to their preferences.
- Welcome Message: Uses large font to display a welcome message.
- Check-in: Users can earn points based on daily check-in, and there is only one opportunity per day
- Personal Information: Displays user's ID, age, and other basic information.
- Statistics: Shows user's post count, threads created, likes received, etc.
- Action Buttons: Includes "Edit Profile" and "Shop" buttons, colored green and yellow respectively.
- Logout: Users can logout and then back to the homepage.
- Shop: The SHOP has different values of the avatar, users can use their own points to buy.

### Contact Page Design
- Team Member Contact Information: Shows team member names, email addresses, and phone numbers.
- Message Form: Users can fill in their name, email, and message to provide feedback or suggestions.
- Send Button: Green "Send Message" button that is easy to notice and click.

### Question Detail Page Design
- Question Content: Displays the question title in large font with detailed content below.
- Answer Form: Users can submit their answers via a textarea and submit button.
- Existing Answers: Lists all answers, including the answer content, author, and timestamp.






instructions for how to launch the application.


Steps to Launch the Application

1.Download the App Folder from GitHub to Your Desktop

2.Navigate to your GitHub repository and download the app folder to your Desktop. Open Visual Studio and Launch the Terminal


3.Change Directory to the App Folder on Your Desktop. In the terminal, navigate to the app folder on your Desktop. code as bellow:

cd C:\Users\...\Desktop\app-folder-name


4.Create and Activate a Virtual Environment
Create a virtual environment:   python -m venv venv
Activate the virtual environment:   venv\Scripts\activate


5.Create a requirements.txt file with the following content:

alembic==1.13.1
blinker==1.8.2
click==8.1.7
colorama==0.4.6
dnspython==2.6.1
email_validator==2.1.1
Flask==3.0.3
Flask-Login==0.6.3
Flask-Mail==0.9.1
Flask-Migrate==4.0.7
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.1
greenlet==3.0.3
idna==3.7
itsdangerous==2.0.1
Jinja2==3.1.4
Mako==1.3.3
MarkupSafe==2.1.5
SQLAlchemy==2.0.30
typing_extensions==4.11.0
Werkzeug==3.0.3
WTForms==3.1.2



6.Install the packages listed in requirements.txt:

pip install -r requirements.txt



7.Initialize the database:    flask db init

Create the first migration:   flask db migrate -m "Initial migration"

Apply the migration:   flask db upgrade

If you encounter any errors, you can downgrade the migration:    flask db downgrade



8.Open the Flask shell:  flask shell



9.Run the following code to import the default 12 zodiac avatars:


from your_app import db
from your_app.models import Avatar 

animals = ['rat', 'ox', 'tiger', 'rabbit', 'dragon', 'snake', 'horse', 'sheep', 'monkey', 'rooster', 'dog', 'pig']

for animal in animals:
    filename = f'{animal}.png'
    path = f'/static/profile-pictures/{filename}'
    if not Avatar.query.filter_by(filename=filename).first():
        avatar = Avatar(filename=filename, path=path)
        db.session.add(avatar)

db.session.commit()




10. In the Flask shell, run the following code to import product data:

from app import db
from app.models import Product

def calculate_price(index):
    if index == 1:
        return 100
    elif index == 2:
        return 200
    elif 3 <= index <= 10:
        return 300
    else:
        return 300 + ((index - 11) // 10) * 300

def add_products():
    db.session.query(Product).delete()

    for i in range(1, 67):
        name = f'Product {i}'
        image_url = f'/static/profile-pictures/shop{i}.jpg'
        price = calculate_price(i)
        product = Product(name=name, image_url=image_url, price=price)
        db.session.add(product)

    db.session.commit()

add_products()



11.Finally, run the application: flask run



Follow these steps to set up and launch your application successfully.






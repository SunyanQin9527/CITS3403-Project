from app import db
from app.models import *

group1 = Group()


P1 = Student(uwa_id = "01234561", name = "People1")
P2 = Student(uwa_id = "01234562", name = "People2")
P3 = Student(uwa_id = "01234563", name = "People3")	
P4 = Student(uwa_id = "01234564", name = "People4")

db.session.add_all([group1,P1,P2,P3,P4])
db.session.commit()



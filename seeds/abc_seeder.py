from flask_seeder import Seeder,generator
from app.models.user import User
from flask_sqlalchemy import SQLAlchemy 
from app import db
from werkzeug.security import generate_password_hash
import uuid

class demoseeder(Seeder):

    def run(self):
        user =User(
                first_name= "ADESH",
                primary_email="admin@project.com",
                primary_phone="9876543210",
                pin=generate_password_hash(str(0000000),method="sha256"),
                uuid = uuid.uuid4()
                )
        db.session.add(user)
        db.session.commit()    
        print("User created.")
    

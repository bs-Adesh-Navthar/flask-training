from flask_seeder import Seeder
from app.models.user import User
from app import db
from werkzeug.security import generate_password_hash
import uuid
from sqlalchemy.exc import IntegrityError

class create_admin(Seeder):
    
    def run(self):
        existing_user = User.query.filter_by(primary_email='admin@project.com').first()
        if existing_user:
            print(f"{existing_user.primary_email}  Email already exists.")
        else:
            try:
                user =User(
                        first_name= "ADMIN",
                        primary_email="admin@project.com",
                        primary_phone="9876543210",
                        pin=generate_password_hash("12345",method="sha256"),
                        uuid = str(uuid.uuid4())
                        )
                db.session.add(user)
                db.session.commit()
            except IntegrityError as e:
                print(f"Error: {e}")
            else:
                print("Admin created successfully.")
        

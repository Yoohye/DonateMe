from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash
from datetime import datetime

DATABASE_URI = 'mysql+pymysql://username:password@localhost/donateme_db'
engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False, index=True)
    is_phone_verified = Column(Boolean, default=False)
    sms_verification_code = Column(String(6))
    phone_verification_attempts = Column(Integer, default=0)
    last_known_latitude = Column(Float)
    last_known_longitude = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

# Additional code for handling user registration, verification, etc.

def send_verification_sms(phone_number):
    # Your logic to send a verification SMS
    pass

def verify_sms_code(phone_number, verification_code):
    # Your logic to verify the SMS code
    pass

def register_user(username, email, password, phone_number, gps_latitude, gps_longitude):
    # Hash the password
    password_hash = generate_password_hash(password)
    # Create a new user instance
    new_user = User(
        username=username,
        email=email,
        hashed_password=password_hash,
        phone_number=phone_number,
        last_known_latitude=gps_latitude,
        last_known_longitude=gps_longitude,
    )
    # Add the new user to the session
    session.add(new_user)
    try:
        # Attempt to commit the new user to the database
        session.commit()
        # Send a verification SMS to the user's phone number
        send_verification_sms(phone_number)
    except SQLAlchemyError as e:
        # If there's an error, roll back the session
        session.rollback()
        print("An error occurred:", e)
    finally:
        # Always close the session
        session.close()

def verify_user_phone(user_id, verification_code):
    # Retrieve the user from the database
    user = session.query(User).get(user_id)
    if user:
        # Verify the SMS code
        if verify_sms_code(user.phone_number, verification_code):
            # Update the user's verification status
            user.is_phone_verified = True
            try:
                session.commit()
                print(f"User {user.username} has been verified.")
            except SQLAlchemyError as e:
                session.rollback()
                print("An error occurred:", e)
        else:
            print("Invalid verification code.")
    else:
        print("User not found.")
    session.close()
<<<<<<< HEAD

=======
>>>>>>> b3c05424b6cc264d7d52e080fa1ddd480c0552b8

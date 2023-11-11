from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

print("Script started")  # Confirm the script is running

DATABASE_URI = 'mysql+pymysql://root:%40Ti123123@localhost/donateme_db'
engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    location = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

Session = sessionmaker(bind=engine)
session = Session()

try:
    new_user = User(
        username='Another User',
        email='another@example.com',
        password='another_hashed_password',
        location='Another Location',
    )
    session.add(new_user)
    session.commit()
    print(f"Added new user: {new_user.username}")

    users = session.query(User).all()
    print("Users in the database:")
    for user in users:
        print(user.username, user.email)

except SQLAlchemyError as e:
    print("An error occurred during the database transaction:", e)
    session.rollback()

finally:
    session.close()
    print("Session closed")  # Confirm that the session is closed

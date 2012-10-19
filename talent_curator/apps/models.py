from sqlalchemy import Column, Integer, String
from talent_curator.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    oauth_token = Column(String(200))
    oauth_secret = Column(String(200))

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return "User[email=%s]" % self.email

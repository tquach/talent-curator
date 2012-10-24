from sqlalchemy import Column, Integer, String
from talent_curator.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    name = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))

    def __init__(self, email, name, first_name, last_name):
        self.email = email
        self.name = name
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "User[email=%s, name=%s, first_name=%s, last_name=%s]" % (self.email, self.name, self.first_name, self.last_name)

from sqlalchemy import Column, Integer, String
from talent_curator.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    userid = Column(String)

    def __init__(self, userid):
        self.userid = userid

    def __repr__(self):
        return "User[userid=%s]" % self.userid

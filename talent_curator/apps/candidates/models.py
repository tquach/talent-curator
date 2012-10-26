from sqlalchemy import Column, Integer, String
from talent_curator.database import Base


class Candidate(Base):
    __tablename__ = 'candidates'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    document_id = Column(String(256))

    def __init__(self, document_id, first_name, last_name=None, *args, **kwargs):
        self.document_id = document_id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "Candidate[id=%s]" % self.id

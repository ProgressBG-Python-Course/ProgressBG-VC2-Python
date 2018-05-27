from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Date
from base import Base

engine = create_engine('sqlite:///:memory:')
# engine.execute("select 'Hello, World!'").scalar()

class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthday = Column(Date)

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday



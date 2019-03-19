# Following steps from https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
import sqlalchemy
from sqlalchemy import create_engine, Table ,MetaData
from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

def __repr__(self):
    return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)

User.__table__
Table('users', MetaData(bind=None),
            Column('id', Integer(), table='users', primary_key=True, nullable=False),
            Column('name', String(), table='users'),
            Column('fullname', String(), table='users'),
            Column('nickname', String(), table='users'), schema=None)

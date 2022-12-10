from sqlalchemy import create_engine, Column, Integer, String, BOOLEAN, DateTime,Text
from sqlalchemy.orm import declarative_base, sessionmaker

from sqlalchemy.inspection import inspect
from os import environ

from sqlalchemy.ext.declarative import DeclarativeMeta


sqlalchemy_database_uri = environ.get('SQLALCHEMY_DATABASE_URI')
#sqlalchemy_database_uri = 'postgresql://tempuser_local:temppassword_local@postgres_linenotify_local/local_testdb'

print(f'url:{sqlalchemy_database_uri}')

engine = create_engine(sqlalchemy_database_uri, echo=True, future=True)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()
Base.metadata.schema = 'notification'

# extension method for serialize sql objects


class Serializer(object):
    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]


class UserToken(Base, Serializer):
    __tablename__ = "user_token"
    id = Column(Integer, primary_key=True)
    target_name = Column(String)
    access_token = Column(String)
    status = Column(BOOLEAN)
    created_dt = Column(DateTime)
    created_by = Column(String)
    modified_dt = Column(DateTime)
    modified_by = Column(String)

    def serialize(self):
        d = Serializer.serialize(self)
        return d

    def __repr__(self):
        return f"User(id={self.id!r}, target_name={self.target_name!r})"


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String, nullable=False)
    # created_at = Column(DateTime, default=datetime.now())
    created_dt = Column(DateTime)
    created_by = Column(String)
    modified_dt = Column(DateTime)
    modified_by = Column(String)
    status = Column(BOOLEAN)

    def __repr__(self) -> str:
        return 'User >>> {self.username}'

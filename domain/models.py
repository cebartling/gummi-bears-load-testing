from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    auth_token = Column(String, nullable=True)

    def __repr__(self):
        return f"<User(last_name='{self.last_name}', first_name='{self.first_name}', username='{self.username}')>"

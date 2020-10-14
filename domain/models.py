from sqlalchemy import Column, String, DateTime, Numeric, Integer, Date
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
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<User(last_name='{self.last_name}', first_name='{self.first_name}', username='{self.username}')>"


class Stock(Base):
    __tablename__ = 'stocks'
    id = Column(UUID, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    symbol = Column(String, nullable=False)
    current_price = Column(Numeric(precision=12, scale=4), nullable=True)
    open_price = Column(Numeric(precision=12, scale=4), nullable=True)
    high_price = Column(Numeric(precision=12, scale=4), nullable=True)
    low_price = Column(Numeric(precision=12, scale=4), nullable=True)
    previous_close_price = Column(Numeric(precision=12, scale=4), nullable=True)
    volume = Column(Integer, nullable=True)
    percent_change = Column(Numeric(precision=12, scale=4), nullable=True)
    price_change = Column(Numeric(precision=12, scale=4), nullable=True)
    latest_trading_date = Column(Date, nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<User(last_name='{self.last_name}', first_name='{self.first_name}', username='{self.username}')>"

import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from domain.models import User, Stock
from util.configuration import get_configuration_value

username = get_configuration_value('GUMMI_BEARS_DB_USERNAME')
password = get_configuration_value('GUMMI_BEARS_DB_PASSWORD')
hostname = get_configuration_value('GUMMI_BEARS_DB_HOSTNAME')
port = get_configuration_value('GUMMI_BEARS_DB_PORT')
database = get_configuration_value('GUMMI_BEARS_DB_DATABASE')
echo_sql_alchemy = get_configuration_value('ECHO_SQLALCHEMY').lower() == 'true'

engine = create_engine(f"postgresql://{username}:{password}@{hostname}:{port}/{database}", echo=echo_sql_alchemy)
session = sessionmaker(bind=engine)()
all_users = session.query(User).all()
all_stocks = session.query(Stock).all()


def random_user():
    return random.choice(all_users)

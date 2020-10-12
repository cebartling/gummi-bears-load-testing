import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from domain.models import User
from util.configuration import get_configuration_value

username = get_configuration_value('GUMMI_BEARS_DB_USERNAME')
password = get_configuration_value('GUMMI_BEARS_DB_PASSWORD')
hostname = get_configuration_value('GUMMI_BEARS_DB_HOSTNAME')
port = get_configuration_value('GUMMI_BEARS_DB_PORT')
database = get_configuration_value('GUMMI_BEARS_DB_DATABASE')


def create_session():
    engine = create_engine(f"postgresql://{username}:{password}@{hostname}:{port}/{database}", echo=True)
    return sessionmaker(bind=engine)()


def random_user():
    session = create_session()
    users = session.query(User).all()
    return random.choice(users)

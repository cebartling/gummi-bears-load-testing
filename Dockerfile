FROM locustio/locust

MAINTAINER chris.bartling@gmail.com

RUN pip install locust locust-plugins python-dotenv sqlalchemy psycopg2-binary



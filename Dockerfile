FROM python:3.8

MAINTAINER chris.bartling@gmail.com

RUN pip install locust locust-plugins python-dotenv sqlalchemy psycopg2-binary

EXPOSE 8089 5557

RUN useradd --create-home locust
USER locust
WORKDIR /home/locust
COPY . /home/locust

ENTRYPOINT ["locust"]

# turn off python output buffering
ENV PYTHONUNBUFFERED=1

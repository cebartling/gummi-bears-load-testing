import logging

from locust import SequentialTaskSet, task, constant

from domain.sqlalchemy import random_user
from graphql.queries import notifications_by_user_id_query, get_all_stocks_query, get_all_metrics_query
from util.http_utils import create_headers, graphql_url, create_graphql_json


class GummiBearsTaskSet(SequentialTaskSet):
    wait_time = constant(1)
    gummi_bear_user = None

    def on_start(self):
        self.gummi_bear_user = random_user()

    def on_stop(self):
        self.gummi_bear_user = None

    @task
    def get_notifications(self):
        logging.info('Retrieving user notifications...')
        query = notifications_by_user_id_query
        variables = {'userId': self.gummi_bear_user.id}
        with self.client.post(url=graphql_url(),
                              json=(create_graphql_json(query, variables)),
                              headers=(create_headers(self.gummi_bear_user.auth_token))) as response:
            if response.status_code != 200:
                response.failure()

    @task
    def get_all_stocks(self):
        logging.info('Retrieving stocks...')
        query = get_all_stocks_query
        variables = {}
        with self.client.post(url=graphql_url(),
                              json=(create_graphql_json(query, variables)),
                              headers=(create_headers(self.gummi_bear_user.auth_token))) as response:
            if response.status_code != 200:
                response.failure()

    @task
    def get_all_metrics(self):
        logging.info('Retrieving metrics...')
        query = get_all_metrics_query
        variables = {}
        with self.client.post(url=graphql_url(),
                              json=(create_graphql_json(query, variables)),
                              headers=(create_headers(self.gummi_bear_user.auth_token))) as response:
            if response.status_code != 200:
                response.failure()


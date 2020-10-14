import uuid

from locust import SequentialTaskSet, task

from domain.sqlalchemy import random_user
from graphql.queries import notifications_by_user_id_query, get_all_stocks_query, get_all_metrics_query
from util.http_utils import create_headers, graphql_url, create_graphql_json


class GummiBearsTaskSet(SequentialTaskSet):

    # def __init__(self, *args, **kwargs):
    #     super(SequentialTaskSet, self).__init__(*args, **kwargs)
    #     Each locust user gets a different id
        # self.random_id = str(uuid.uuid4())

    # user = None

    # def on_start(self):
    #     self.user = random_user()

    @task
    def get_notifications(self):
        user = random_user()
        query = notifications_by_user_id_query
        variables = {'userId': user.id}
        with self.client.post(url=graphql_url(),
                              json=(create_graphql_json(query, variables)),
                              headers=(create_headers(user.auth_token))) as response:
            if response.status_code != 200:
                response.failure()

    @task
    def get_all_stocks(self):
        user = random_user()
        query = get_all_stocks_query
        variables = {}
        with self.client.post(url=graphql_url(),
                              json=(create_graphql_json(query, variables)),
                              headers=(create_headers(user.auth_token))) as response:
            if response.status_code != 200:
                response.failure()

    @task
    def get_all_metrics(self):
        user = random_user()
        query = get_all_metrics_query
        variables = {}
        with self.client.post(url=graphql_url(),
                              json=(create_graphql_json(query, variables)),
                              headers=(create_headers(user.auth_token))) as response:
            if response.status_code != 200:
                response.failure()

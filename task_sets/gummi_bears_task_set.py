import json

from locust import SequentialTaskSet, task

from domain.sqlalchemy import random_user
from util.http_utils import create_headers, graphql_url, create_graphql_json


class GummiBearsTaskSet(SequentialTaskSet):

    @task
    def get_notifications(self):
        user = random_user()
        query = """
            query UserNotifications($userId: ID!) {
               notificationsByUserId(userId: $userId) {
                  id   
                  message
                  read
                  notificationTimestamp
               }
            }
        """
        variables = {'userId': user.id}
        with self.client.post(url=graphql_url(),
                              json=(create_graphql_json(query, variables)),
                              headers=(create_headers(user.auth_token))) as response:
            if response.status_code != 200:
                print(f'FAILURE: Response status code: {response.status_code}')

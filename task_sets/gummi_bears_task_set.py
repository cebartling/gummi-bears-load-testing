from locust import SequentialTaskSet, task

from domain.sqlalchemy import random_user


class GummiBearsTaskSet(SequentialTaskSet):
    @task
    def view_welcome(self):
        user = random_user()
        print(f'Random auth token: {user.auth_token}')
        with self.client.get(url='/') as response:
            if response.status_code != 200:
                print(f'FAILURE: Response status code: {response.status_code}')

    # @task
    # def view_sign_in(self):
    #     print(f'GummiBearsBehaviors ({self!r}) executing view_welcome')
    #     with self.client.get(url="/") as response:
    #         if response.status_code != 200:
    #             print(f'FAILURE: Response status code: {response.status_code}')

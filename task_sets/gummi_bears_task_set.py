from locust import SequentialTaskSet, task


class GummiBearsTaskSet(SequentialTaskSet):
    @task
    def view_welcome(self):
        print(f'GummiBearsBehaviors ({self!r}) executing view_welcome')
        with self.client.get(url='/') as response:
            if response.status_code != 200:
                print(f'FAILURE: Response status code: {response.status_code}')

    # @task
    # def view_sign_in(self):
    #     print(f'GummiBearsBehaviors ({self!r}) executing view_welcome')
    #     with self.client.get(url="/") as response:
    #         if response.status_code != 200:
    #             print(f'FAILURE: Response status code: {response.status_code}')

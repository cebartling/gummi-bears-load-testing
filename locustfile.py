from locust import HttpUser

from task_sets.gummi_bears_task_set import GummiBearsTaskSet


class GummiBearsUser(HttpUser):
    min_wait = 1000
    max_wait = 2000
    tasks = [GummiBearsTaskSet]

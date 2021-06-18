
import time
from locust import HttpUser, task, between

class LoadTestAsyncDjango(HttpUser):
    wait_time = between(1, 1)

    @task
    def get_async(self):
        self.client.get("/async")

    def on_start(self):
        pass
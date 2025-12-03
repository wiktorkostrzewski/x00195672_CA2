from locust import HttpUser, task, between

class CalculatorUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def add_numbers(self):
        self.client.post("/", data={
            "first": "24",
            "second": "26",
            "operation": "add"
        })
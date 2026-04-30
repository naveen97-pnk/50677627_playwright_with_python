import requests
from config.env import Env

class ApiClient:

    @staticmethod
    def get(endpoint, headers=None):
        return requests.get(f"{Env.API_BASE_URL}{endpoint}", headers=headers)

    @staticmethod
    def post(self, endpoint, payload, headers=None):
        return requests.post(f"{Env.API_BASE_URL}{endpoint}", headers=headers)
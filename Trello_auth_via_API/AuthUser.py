import requests
import json


class AuthUser:
    url = 'https://trello.com/1/authentication'
    headers = {'Content-Type': 'application/json; charset=utf-8'
               }
    response = None

    def __init__(self):
        pass

    def send_request(self, payload):
        self.response = requests.post(
            self.url,
            data=json.JSONEncoder().encode(payload),
            headers=self.headers
        )

import requests
from framework.utils.config_parser import config
import ast


class API:

    def __init__(self):
        self._response = None

    def get(self, url: str) -> requests.Response:
        self._response = requests.get(config["base_url"] + url)
        return self._response

    def delete(self, url: str) -> requests.Response:
        self._response = requests.post(config["base_url"] + url)
        return self._response

    def post(self, url: str, body: dict) -> requests.Response:
        self._response = requests.post(config["base_url"] + url, data=body)
        return self._response

    def put(self, url: str, body: dict) -> requests.Response:
        self._response = requests.put(config["base_url"] + url, data=body)
        return self._response

    def patch(self, url: str, body: dict) -> requests.Response:
        self._response = requests.patch(config["base_url"] + url, data=body)
        return self._response

    def get_text_response(self) -> dict:
        return ast.literal_eval(self._response.text)

    def get_status_code(self) -> str:
        return self._response.status_code

import requests
from config.conftest import start_test, end_test


def test(start_test, end_test):
    page = requests.get('http://localhost:3000/user/login')

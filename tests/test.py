import requests
from config.conftest import start_test, end_test
from framework.utils.config_parser import config


def test(start_test, end_test):
    assert requests.get(config['base_url']).status_code == 200

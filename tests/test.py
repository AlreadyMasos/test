import requests
from config.conftest import start_test, end_test
from framework.utils.config_parser import config
from page_objects.HomePage import HomePage
from framework.API.api import API
import pytest


@pytest.mark.parametrize("name, code", [('first', '200'),
                                        ('second', '200')])
def test_status_code(start_test, end_test, name, code):
    assert requests.get(config['base_url']).status_code == 200
    home_page = HomePage()
    home_page.click_on_button_by_name(name)
    assert home_page.check_code(code)


@pytest.mark.parametrize('endpoint, result', [])
def test_check_api_positive(start_test, end_test, endpoint, result):
    page = HomePage()
    api = API()
    api.get(endpoint)
    assert page.get_dict_response() == api.get_text_response()


@pytest.mark.parametrize('endpoint, result', [])
def test_check_api_negative(start_test, end_test, result, endpoint):
    page = HomePage()
    api = API()
    api.get(endpoint)
    assert page.get_dict_response() == api.get_text_response()

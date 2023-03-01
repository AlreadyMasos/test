import requests
from config.conftest import start_test, end_test
from framework.utils.string_util import check_dict_equals
from page_objects.HomePage import HomePage
from framework.API.api import API
from test_data.test_data import *
import pytest


@pytest.mark.parametrize('name, endpoint', GET_DATA)
def test_check_get_api(start_test, end_test, endpoint, name):
    page = HomePage()
    api = API()
    api.get(endpoint)
    page.click_on_button_by_name(name)
    assert check_dict_equals(page.get_dict_response(), api.get_text_response())


@pytest.mark.parametrize('body, endpoint, status_code, result', POST_DATA)
def test_check_api_post(body, endpoint, status_code, result):
    api = API()
    api.post(endpoint, body)
    assert api.get_status_code() == status_code
    assert check_dict_equals(result, api.get_text_response())


@pytest.mark.parametrize("name, code", FIRST_TEST_DATA)
def ui_tests(start_test, end_test, name, code):
    home_page = HomePage()
    home_page.click_on_button_by_name(name)
    assert home_page.check_code(code)

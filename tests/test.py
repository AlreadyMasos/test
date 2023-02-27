import requests
from config.conftest import start_test, end_test
from framework.utils.config_parser import config
from page_objects.HomePage import HomePage
import pytest


@pytest.mark.parametrize("name, code", [('first', '200'),
                                        ('second', '200')])
def test(start_test, end_test, name, code):
    assert requests.get(config['base_url']).status_code == 200
    home_page = HomePage()
    home_page.click_on_button_by_name(name)
    home_page.check_code(code)


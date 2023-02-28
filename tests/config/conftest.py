import pytest
from framework.browser.browser import Browser
from framework.utils.config_parser import config


@pytest.fixture
def start_test():
    Browser().set_up_driver()
    Browser().maximize()
    Browser().set_url(config['base_url'])


@pytest.fixture
def end_test(request):
    def deleter():
        Browser().quit()
    request.addfinalizer(deleter)

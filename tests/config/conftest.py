import pytest
from framework.browser.browser import Browser


@pytest.fixture(autouse=True)
def start_test():
    Browser().set_up_driver()
    Browser().maximize()
    Browser().set_url('https://reqres.in')


@pytest.fixture(autouse=True)
def end_test(request):
    def deleter():
        Browser().quit()
    request.addfinalizer(deleter)

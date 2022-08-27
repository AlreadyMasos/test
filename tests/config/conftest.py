import os
import pytest
import requests
from time import sleep
from framework.browser.browser import Browser


@pytest.fixture(scope='session')
def start_test():
    os.system('docker-compose up -d')
    sleep(10)
    Browser().set_url('http://localhost:3000/user/login')


@pytest.fixture(scope='session')
def end_test(request):
    def quit():
        os.system('docker container kill gitea')
        os.system('docker container kill test_task_gitea_db_1')
        Browser().quit()
    request.addfinalizer(quit)

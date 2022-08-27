import requests
from page_objects.LoginPage import LoginPage
from page_objects.RegisterPage import RegisterPage


def test(start_test):
    page = requests.get('http://localhost:3000/user/login')
    assert page.status_code == 200, 'wrong port'
    assert 'OpenID' in page.text, 'wrong text'

    login_page = LoginPage()
    assert login_page.is_opened(), 'login page not opened'

    login_page.click_reg_button()
    register_page = RegisterPage()
    assert register_page.is_opened(), 'reg page not opened'

    register_page.insert_email()
    register_page.insert_usr_name()
    register_page.insert_password()
    register_page.click_create_page_button()


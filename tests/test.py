import requests
from page_objects.LoginPage import LoginPage
from page_objects.RegisterPage import RegisterPage
from page_objects.UserPage import UserPage
from page_objects.CreateRepoPage import CreateRepoPage
from page_objects.RepoPage import RepoPage
from page_objects.CreateFilePage import CreateFilePage
from page_objects.NewFilePage import NewFilePage
from config.conftest import start_test, end_test


def test(start_test, end_test):
    page = requests.get('http://localhost:3000/user/login')
    assert page.status_code == 200, 'wrong port'
    assert 'OpenID' in page.text, 'wrong text'

    login_page = LoginPage()
    assert login_page.is_opened(), 'login page not opened'

    login_page.click_reg_button()
    register_page = RegisterPage()
    assert register_page.is_opened(), 'reg page not opened'

    register_page.insert_email()
    usr_name = register_page.insert_usr_name()
    register_page.insert_password()
    register_page.click_create_page_button()
    user_page = UserPage()
    assert user_page.is_opened(), 'usr page not opened'
    assert user_page.check_correct_user(usr_name), 'wrong user name'

    user_page.click_new_repo()
    create_repo_page = CreateRepoPage()
    assert create_repo_page.is_opened(), 'create repo page not opened'
    assert create_repo_page.check_correct_owner(usr_name), 'wrong repo owner'

    create_repo_page.insert_repo_name()
    create_repo_page.click_create_repo()
    repo_page = RepoPage()
    assert repo_page.is_opened(), 'repo page not opened'

    repo_page.click_new_file()
    create_file_page = CreateFilePage()
    create_file_page.is_opened(), 'create file page not opened'
    create_file_page.insert_file_name()
    file_text = create_file_page.insert_file_text()
    create_file_page.click_commit_button()
    new_file_page = NewFilePage()
    assert new_file_page.check_text_file(file_text), 'wrong text'

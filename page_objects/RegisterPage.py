from framework.pages.base_page import BasePage
from framework.elements.text_box import TextBox
from framework.elements.button import Button
from framework.utils.string_util import set_random_string, set_random_email


class RegisterPage(BasePage):

    USR_NAME_INPUT = TextBox('xpath', '//input[@id="user_name"]', 'insert_usr_name')
    EMAIL_INPUT = TextBox('xpath', '//input[@id="email"]', 'insert_usr_name')
    PASSWORD_INPUT = TextBox('xpath', '//input[@id="password"]', 'insert_password')
    PASSWORD_AGAIN_INPUT = TextBox('xpath', '//input[@id="retype"]', 'insert_password')
    CREATE_PAGE_BUTTON = Button('xpath', '//button[@class="ui green button"]', 'create_page')

    def __init__(self):
        super().__init__(self.CREATE_PAGE_BUTTON.get_search_condition(),
                         self.CREATE_PAGE_BUTTON.get_locator(),
                         self.CREATE_PAGE_BUTTON.get_name())

    def insert_usr_name(self):
        usr_name = set_random_string(7)
        self.USR_NAME_INPUT.send_text(usr_name)
        return usr_name

    def insert_email(self):
        self.EMAIL_INPUT.send_text(set_random_email(5))

    def insert_password(self):
        random_password = set_random_string(8)
        self.PASSWORD_INPUT.send_text(random_password)
        self.PASSWORD_AGAIN_INPUT.send_text(random_password)

    def click_create_page_button(self):
        self.CREATE_PAGE_BUTTON.click()

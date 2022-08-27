from framework.pages.base_page import BasePage
from framework.elements.text_box import TextBox
from framework.elements.button import Button


class LoginPage(BasePage):

    USR_NAME_INPUT = TextBox('xpath', '//input[@id="user_name"]', 'insert_usr_name')
    PASSWORD_INPUT = TextBox('xpath', '//input[@id="password"]', 'insert_password')

    REG_BUTTON = Button('xpath', '//div[@class="right stackable menu"]//a[@href="/user/sign_up"]',
                        'reg_button')

    def __init__(self):
        super().__init__(self.REG_BUTTON.get_search_condition(),
                         self.REG_BUTTON.get_locator(),
                         self.REG_BUTTON.get_name())

    def click_reg_button(self):
        self.REG_BUTTON.click()

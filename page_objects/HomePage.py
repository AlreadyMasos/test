from framework.pages.base_page import BasePage
from framework.elements.text_box import TextBox
from framework.utils.string_util import set_random_string
from framework.elements.button import Button
import ast


class HomePage(BasePage):

    def __init__(self):
        super().__init__(self.RESPONSE.get_search_condition(),
                         self.RESPONSE.get_locator(),
                         self.RESPONSE.get_name())

    RESPONSE = TextBox('xpath',
                       '//span[@class="response-code"]',
                       'response code')

    RESPONSE_DATA = TextBox('xpath',
                            '//pre[@data-key="output-response"]',
                            'response data')

    GET_LIST_USERS = Button('xpath',
                            '//li[@data-id="users"]',
                            '1')

    GET_SINGLE_USER = Button('xpath',
                             '//li[@data-id="users-single"]',
                             '2')

    GET_SINGLE_USER_NOT_FOUND = Button('xpath',
                                       '//li[@data-id="users-single"]',
                                       '3')

    LIST_RES = Button('xpath',
                      '//li[@data-id="unknown"]',
                      '4')

    SINGLE_RES = Button('xpath',
                        '//li[@data-id="unknown-single"]',
                        '5')

    SINGLE_NOT_FOUND = Button('xpath',
                              '//li[@data-id="unknown-single-not-found"]',
                              '6')

    POST = Button('xpath',
                  '//li[@data-id="post"]',
                  '7')

    PUT = Button('xpath',
                 '//li[@data-id="put"]',
                 '8')

    PATCH = Button('xpath',
                   '//li[@data-id="patch"]',
                   '9')

    DELETE = Button('xpath',
                    '//li[@data-id="delete"]',
                    '10')

    REG_SUC = Button('xpath',
                     '//li[@data-id="register-successful"]',
                     '11')

    REG_UNSUC = Button('xpath',
                       '//li[@data-id="register-unsuccessful"]',
                       '12')

    LOGIN_SUC = Button('xpath',
                       '//li[@data-id="login-successful"]',
                       '13')

    LOGIN_UNSUC = Button('xpath',
                         '//li[@data-id="login-unsuccessful"]',
                         '14')

    DELAYED_RESPONSE = Button('xpath',
                              '//li[@data-id="delay"]',
                              '15')

    LIST_OF_ALL_BUTTONS = [GET_LIST_USERS, GET_SINGLE_USER_NOT_FOUND,
                           POST, DELETE, REG_SUC, REG_UNSUC,
                           LOGIN_SUC, LOGIN_UNSUC, DELAYED_RESPONSE]

    def click_on_button_by_name(self, name: str):
        for btn in self.LIST_OF_ALL_BUTTONS:
            if btn.get_name() == name:
                btn.click()

    def get_response_status_code(self) -> str:
        return self.RESPONSE.get_text()

    def check_code(self, code: str) -> bool:
        return self.get_response_status_code() == code

    def get_dict_response(self):
        return ast.literal_eval(self.RESPONSE_DATA.get_text())

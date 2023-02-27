from framework.pages.base_page import BasePage
from framework.elements.text_box import TextBox
from framework.utils.string_util import set_random_string
from framework.elements.button import Button


class HomePage(BasePage):

    def __init__(self):
        super().__init__(self.RESPONSE.get_search_condition(),
                         self.RESPONSE.get_locator(),
                         self.RESPONSE.get_name())

    RESPONSE = TextBox('xpath',
                       'class="response-code"',
                       'response code')

    GET_LIST_USERS = Button('xpath',
                            '//li[@data-id="users"]',
                            'first')

    GET_SINGLE_USER = Button('xpath',
                             '//li[@data-id="users-single"]',
                             'second')

    GET_SINGLE_USER_NOT_FOUND = Button('xpath',
                                       '//li[@data-id="users-single"]',
                                       'get list users btn')

    POST = Button('xpath',
                  '//li[@data-id="post"]',
                  'create user button')

    PUT = Button('xpath',
                 '//li[@data-id="put"]',
                 'update user button')

    PATCH = Button('xpath',
                   '//li[@data-id="patch"]',
                   'patch user button')

    DELETE = Button('xpath',
                    '//li[@data-id="delete"]',
                    'delete user button')

    REG_SUC = Button('xpath',
                     '//li[@data-id="register-successful"]',
                     'successful reg')

    REG_UNSUC = Button('xpath',
                       '//li[@data-id="register-unsuccessful"]',
                       'unsuccessful reg')

    LOGIN_SUC = Button('xpath',
                       '//li[@data-id="login-successful"]',
                       'successful login')

    LOGIN_UNSUC = Button('xpath',
                         '//li[@data-id="login-unsuccessful"]',
                         'unsuccessful login')

    DELAYED_RESPONSE = Button('xpath',
                              '//li[@data-id="delay"]',
                              'delay response')

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

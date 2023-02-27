from framework.pages.base_page import BasePage
from framework.elements.text_box import TextBox
from framework.utils.string_util import set_random_string
from framework.elements.button import Button


class HomePage(BasePage):
    RESPONSE = TextBox('xpath',
                       'class="response-code"',
                       'response code')

    GET_LIST_USERS = Button('xpath',
                            '//li[@data-id="users"]',
                            'get list users btn')

    GET_SINGLE_USER = Button('xpath',
                             '//li[@data-id="users-single"]',
                             'get list users btn')

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

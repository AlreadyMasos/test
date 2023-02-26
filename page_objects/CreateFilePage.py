from framework.pages.base_page import BasePage
from framework.elements.text_box import TextBox
from framework.utils.string_util import set_random_string
from framework.elements.button import Button


class HomePage(BasePage):

    GET_LIST_USERS = Button('xpath',
                            '//li[@data-id="users"]',
                            'get list users btn')
    GET_SINGLE_USER = Button('xpath',
                             '//li[@data-id="users-single"]',
                             'get list users btn')
    GET_SINGLE_USER_NOT_FOUND = Button('xpath',
                                       '//li[@data-id="users-single"]',
                                       'get list users btn')

from framework.pages.base_page import BasePage
from framework.elements.text import Text
from framework.elements.button import Button


class UserPage(BasePage):

    USER_NAME = Text('xpath', '//span[@class="text truncated-item-container"]//span', 'name')
    NEW_REPO_BUTTON = Button('xpath', '//a[@data-content="New Repository"]', 'new_rep_btn')

    def __init__(self):
        super().__init__(self.NEW_REPO_BUTTON.get_search_condition(),
                         self.NEW_REPO_BUTTON.get_locator(),
                         self.NEW_REPO_BUTTON.get_name())

    def check_correct_user(self, name):
        return self.USER_NAME.get_text() == name

    def click_new_repo(self):
        self.NEW_REPO_BUTTON.click()

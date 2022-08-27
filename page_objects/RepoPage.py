from framework.pages.base_page import BasePage
from framework.elements.button import Button


class RepoPage(BasePage):

    NEW_FILE = Button('xpath', "//a[contains(text(),'New File')]", 'new_file')

    def __init__(self):
        super().__init__(self.NEW_FILE.get_search_condition(),
                         self.NEW_FILE.get_locator(),
                         self.NEW_FILE.get_name())

    def click_new_file(self):
        self.NEW_FILE.click()

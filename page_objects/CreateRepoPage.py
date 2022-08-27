from framework.pages.base_page import BasePage
from framework.elements.text_box import TextBox
from framework.elements.text import Text
from framework.utils.string_util import set_random_string
from framework.elements.button import Button


class CreateRepoPage(BasePage):

    REPO_NAME = TextBox('xpath', '//input[@id="repo_name"]', 'repo_name')
    OWNER_NAME = Text('xpath', '//span//span[@class="truncated-item-name"]', 'own_name')
    CREATE_BUTTON = Button('xpath', '//button[@class="ui green button"]', 'create_button')
    FILES_CHECKBOX = Button('xpath', '//label[contains(text(),"Ini")]', 'files_checkbox')

    def __init__(self):
        super().__init__(self.REPO_NAME.get_search_condition(),
                         self.REPO_NAME.get_locator(),
                         self.REPO_NAME.get_name())

    def check_correct_owner(self, name):
        return self.OWNER_NAME.get_text() == name

    def insert_repo_name(self):
        repo_name = set_random_string(6)
        self.REPO_NAME.send_text(repo_name)
        return repo_name

    def click_create_repo(self):
        self.FILES_CHECKBOX.click()
        self.CREATE_BUTTON.click()

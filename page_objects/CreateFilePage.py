from framework.pages.base_page import BasePage
from framework.elements.text_box import TextBox
from framework.utils.string_util import set_random_string
from framework.elements.button import Button


class CreateFilePage(BasePage):

    FILE_NAME = TextBox('xpath', '//input[@id="file-name"]', 'file name')
    TEXT_BUTTON = Button('xpath', '//div[@class="monaco-editor-container"]', 'txt btn')
    TEXTAREA = TextBox('xpath', '//textarea[@class="inputarea monaco-mouse-cursor-text"]', 'textarea')
    COMMIT_BUTTON = Button('xpath', '//button[@id="commit-button"]', '//button[@id="commit-button"]')

    def __init__(self):
        super().__init__(self.FILE_NAME.get_search_condition(),
                         self.FILE_NAME.get_locator(),
                         self.FILE_NAME.get_name())

    def insert_file_name(self):
        file_name = set_random_string(8)
        self.FILE_NAME.send_text(file_name)
        return file_name

    def insert_file_text(self):
        file_text = set_random_string(30)
        self.TEXT_BUTTON.click()
        self.TEXTAREA.send_text(file_text)
        return file_text

    def click_commit_button(self):
        self.COMMIT_BUTTON.click()
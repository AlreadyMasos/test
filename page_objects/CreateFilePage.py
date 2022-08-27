from framework.pages.base_page import BasePage
from framework.elements.text_box import TextBox
from framework.utils.string_util import set_random_string


class CreateFilePage(BasePage):

    FILE_NAME = TextBox('xpath', '//input[@id="file-name"]', 'file name')
    TEXTAREA = TextBox('xpath', '//div[@class="monaco-editor-container"]', 'textarea')

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
        self.TEXTAREA.click()
        self.TEXTAREA.send_text(file_text)
        return file_text

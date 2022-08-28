from framework.pages.base_page import BasePage
from framework.elements.text import Text


class NewFilePage(BasePage):

    FILE_TEXT = Text('xpath', '//code[@class="code-inner"]', 'file text')

    def __init__(self):
        super().__init__(self.FILE_TEXT.get_search_condition(),
                         self.FILE_TEXT.get_locator(),
                         self.FILE_TEXT.get_name())

    def check_text_file(self, text):
        return self.FILE_TEXT.get_text() == text

from framework.browser.browser import Browser
from framework.utils.logger import Logger
from framework.elements.text_box import TextBox


class BasePage:
    def __init__(self, search_condition: str, locator: str, page_name: str) -> None:
        self.locator = locator
        self.page_name = page_name
        self.search_condition = search_condition

    def wait_page_to_load(self) -> None:
        Logger.info("Ожидание загрузки страницы " + self.page_name + " с помощью js")
        Browser.get_browser().wait_for_page_to_load()

    def is_opened(self) -> bool:
        Logger.info("Проверка, открыта ли страница " + self.page_name)
        self.wait_page_to_load()
        return Browser.get_browser().is_wait_successful(
            TextBox(self.search_condition, self.locator, self.page_name).wait_for_is_visible)

    def wait_for_page_opened(self) -> None:
        Logger.info("Ожидание загрузки страницы " + self.page_name + " и видимости идентифицирующего ее элемента")
        self.wait_page_to_load()
        TextBox(self.search_condition, self.locator, self.page_name).wait_for_is_visible()

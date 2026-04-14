from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/")

    def go_to_section(self, section_name: str):
        self.page.locator(f"text={section_name}").click()

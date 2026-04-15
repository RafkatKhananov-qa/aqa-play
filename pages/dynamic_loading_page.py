from playwright.sync_api import expect

from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        # локаторы
        self.example_1_link = page.locator("a[href='/dynamic_loading/1']")
        self.start_button = page.locator("button:has-text('Start')")
        self.hello_text = page.locator("h4:has-text('Hello World!')")

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/dynamic_loading")

    def open_example_1(self):
        self.example_1_link.click()

    def click_start(self):
        self.start_button.click()

    def wait_for_hello_text(self):
        expect(self.hello_text).to_be_visible()

    def print_result(self):
        print("✅ Элемент появился: Hello World!")

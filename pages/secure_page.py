from pages.base_page import BasePage


class SecurePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.logout_button = page.locator("//i//ancestor::a")

    def click_logout(self):
        self.logout_button.click()

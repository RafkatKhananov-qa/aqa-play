from pages.base_page import BasePage
from playwright.sync_api import expect


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_button = page.locator("button.radius")
        self.logout_button = page.locator("a.button.secondary.radius")

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def verify_login_success(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/secure")

    def logout(self):
        self.logout_button.click()

    def verify_logout_success(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/login")

    def login_process(self):
        base_page = BasePage(self.page)
        base_page.navigate_to_example("Form Authentication")
        username = self.page.locator("//input[@id='username']")
        username.fill("tomsmith")
        password = self.page.locator("//input[@id='password']")
        password.fill("SuperSecretPassword!")
        login_button = self.page.locator("//button[@class='radius']")
        login_button.click()

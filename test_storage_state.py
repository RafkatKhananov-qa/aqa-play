import time
from playwright.sync_api import Page


def test_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("//input[@id='user-name']").fill("standard_user")
    page.locator("//input[@id='password']").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    page.context.storage_state(path="state.json")


def test_2(browser):
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    page.goto("https://www.saucedemo.com/inventory.html")
    time.sleep(5)



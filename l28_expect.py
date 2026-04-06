from playwright.sync_api import sync_playwright, expect


def test_28_01():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
        start_button = page.locator("//button[text()='Start']")
        start_button.click()
        expect(page.locator("//h4[text()='Hello World!']")).to_be_visible()
        expect(page.locator("//h4[text()='Hello World!']")).to_have_text("Hello World!")


def test_28_02():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
        start_button = page.locator("//button[text()='Start']")
        start_button.click()
        spinner = page.locator("//div[@id='loading']")
        expect(spinner).to_be_hidden()
        expect(page.locator("//h4[text()='Hello World!']")).to_be_visible()
        expect(page.locator("//h4[text()='Hello World!']")).to_have_text("Hello World!")

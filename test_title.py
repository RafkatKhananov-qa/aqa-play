import re
from playwright.sync_api import sync_playwright, expect


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://playwright.dev/python/")
        get_started_link = page.locator("//a[text()='Get started']")
        get_started_link.click()
        expect(page).to_have_url("https://playwright.dev/python/docs/intro")
        expect(page).to_have_title(re.compile(r".*Installation.*"))

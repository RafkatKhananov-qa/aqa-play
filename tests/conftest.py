import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    with sync_playwright() as drv:
        browser = drv.firefox.launch(headless=False)
        page_ = browser.new_page()
        page_.set_default_timeout(7000)
        yield page_
        browser.close()


BASE_URL = "https://the-internet.herokuapp.com/"

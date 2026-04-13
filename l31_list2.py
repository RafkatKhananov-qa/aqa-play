import pytest
from playwright.sync_api import sync_playwright, expect


def test_31_16():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/checkboxes")
        checkboxes = page.locator("//input[@type='checkbox']")
        checkboxes_count = checkboxes.count()
        assert checkboxes_count == 2


def test_31_17():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/checkboxes")
        checkboxes = page.locator("//input[@type='checkbox']")
        checkboxes.first.check()
        expect(checkboxes.first).to_be_checked()
        checkboxes.last.check()
        expect(checkboxes.last).to_be_checked()


def test_31_18():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/checkboxes")
        checkboxes = page.locator("//input[@type='checkbox']")
        count = checkboxes.count()
        for i in range(count):
            checkbox = checkboxes.nth(i)
            if not checkbox.is_checked():
                checkbox.check()
        for i in range(count):
            assert checkboxes.nth(i).is_checked(), f"Checkbox {i} не отмечен"


def test_31_19():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/checkboxes")

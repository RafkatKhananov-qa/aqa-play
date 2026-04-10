import time

import pytest
from playwright.sync_api import sync_playwright, expect


def test_31_01():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
        add_element_button = page.locator("//button[text()='Add Element']")
        add_element_button.click(click_count=3)
        expect(page.locator("//button[text()='Delete']")).to_have_count(3)


def test_31_02():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
        add_element_button = page.locator("//button[text()='Add Element']")
        add_element_button.click(click_count=2)
        delete_button = page.locator("//button[text()='Delete']")
        delete_button.first.click()
        expect(page.locator("//button[text()='Delete']")).to_have_count(1)


def test_31_03():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
        add_element_button = page.locator("//button[text()='Add Element']")
        add_element_button.click(click_count=4)
        delete_button = page.locator("//button[text()='Delete']")
        delete_button.last.click()
        expect(page.locator("//button[text()='Delete']")).to_have_count(3)


def test_31_04():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
        add_element_button = page.locator("//button[text()='Add Element']")
        add_element_button.click(click_count=5)
        delete_button = page.locator("//button[text()='Delete']")
        delete_button.nth(2).click()
        expect(page.locator("//button[text()='Delete']")).to_have_count(4)


def test_31_05():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
        delete_button = page.locator("//button[text()='Delete']")
        expect(delete_button).to_have_count(0)
        expect(delete_button.first).not_to_be_visible()
        expect(delete_button.last).not_to_be_visible()


def test_31_06():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/checkboxes")
        checkbox_1 = page.locator("//input[@type='checkbox'][1]")
        checkbox_1.check()
        expect(checkbox_1).to_be_checked()


def test_31_07():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/checkboxes")
        checkboxes = page.locator("input[type='checkbox']")
        for i in range(checkboxes.count()):
            checkbox = checkboxes.nth(i)
            if not checkbox.is_checked():
                checkbox.check()
        unchecked = page.locator("input[type='checkbox']:not(:checked)")
        expect(unchecked).to_have_count(0)


@pytest.mark.skip("При переходе по URL 404 ошибка")
def test_31_08():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/radio_buttons")


def test_31_09():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/dropdown")
        dropdown = page.locator("//select[@id='dropdown']")
        dropdown.select_option("1")
        expect(dropdown).to_have_value("1")


def test_31_10():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/checkboxes")
        labels = page.locator("#checkboxes").inner_text().splitlines()
        labels = [l.strip() for l in labels if l.strip()]
        print(labels)


def test_31_11():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/dropdown")
        values = page.locator("#dropdown option").evaluate_all(
            "els => els.map(e => e.value)"
        )
        assert values == ["", "1", "2"]


def test_31_12():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/checkboxes")
        checkboxes = page.locator("input[type='checkbox']")
        for i in range(checkboxes.count()):
            if i % 2 == 1:
                checkbox = checkboxes.nth(i)
                checkbox.check()
        expect(page.locator("//input[@type='checkbox'][1]")).not_to_be_checked()
        expect(page.locator("//input[@type='checkbox'][2]")).to_be_checked()


@pytest.mark.skip("При переходе по URL 404 ошибка")
def test_31_13():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/challenging_page")


def test_31_14():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
        start_button = page.locator("//button[text()='Start']")
        start_button.click()
        expect(page.locator("//h4[text()='Hello World!']")).to_be_visible()
        expect(page.locator("//h4[text()='Hello World!']")).to_have_count(1)
        assert page.locator("//h4[text()='Hello World!']").first.text_content() == "Hello World!"


def test_31_15():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/hovers")
        cards = page.locator("//div[@class='figure']")
        expect(cards).to_have_count(3)
        titles = cards.locator("h5").all_inner_texts()
        print(titles)
        card_1 = page.locator("//div[@class='figure'][1]")
        card_1.hover()
        view_profile_link = page.locator("//div[@class='figure'][1]//a")
        view_profile_link.click()
        assert "/users/1" in page.url

import pytest
from playwright.sync_api import sync_playwright, expect


def test_32_1():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
        add_element_button = page.locator("//button[text()='Add Element']")
        add_element_button.click()
        delete_button = page.locator("//button[text()='Delete']")
        expect(delete_button).to_be_visible()
        delete_button.click()
        expect(delete_button).not_to_be_visible()


def test_32_2():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://demoqa.com/buttons")
        page.locator("#doubleClickBtn").dblclick()
        expect(page.locator("#doubleClickMessage")).to_be_visible()


def test_32_3():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://demoqa.com/buttons")
        page.locator("#rightClickBtn").click(button="right")
        expect(page.locator("#rightClickMessage")).to_be_visible()


def test_32_4():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/hovers")

        first_image = page.locator("//div[@class='figure'][1]")
        first_image.hover()

        page.locator("//div[@class='figure'][1]//a[text()='View profile']").click()

        expect(page).to_have_url("https://the-internet.herokuapp.com/users/1")


def test_32_6():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/key_presses")

        target = page.locator("#target")
        result = page.locator("#result")
        header = page.locator("//h3")

        target.press_sequentially("Hello", delay=100)
        header.click()
        page.keyboard.press("Enter")

        expect(result).to_have_text("You entered: ENTER")


def test_32_7():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/key_presses")

        target = page.locator("#target")
        target.focus()
        target.press_sequentially("Hello", delay=100)
        target.press("Control+a")
        target.press("Delete")
        expect(target).to_have_value("")


def test_32_8():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/checkboxes")

        checkbox_1 = page.locator("//input[@type='checkbox'][1]")
        checkbox_1.check()

        checkbox_2 = page.locator("//input[@type='checkbox'][2]")
        checkbox_2.click(modifiers=["Control"])

        expect(checkbox_1).to_be_checked()
        expect(checkbox_2).not_to_be_checked()


def test_32_9():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/drag_and_drop")

        box_a = page.locator("#column-a")
        box_b = page.locator("#column-b")

        box_a.click(position={"x": 10, "y": 10})

        box_a.drag_to(box_b)

        expect(box_a).to_contain_text("B")
        expect(box_b).to_contain_text("A")


def test_32_10():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/inputs")

        input_field = page.locator("//input")
        input_field.focus()

        input_field.fill("4654567567")

        input_field.blur()


def test_32_11():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

        add_element_button = page.locator("//button[text()='Add Element']")
        add_element_button.dispatch_event("click")

        expect(page.locator("//button[text()='Delete']")).to_be_visible()


def test_32_12():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://demoqa.com/text-box")
        source = page.locator("#userName")
        target = page.locator("#userEmail")

        # 1. Ввод текста
        source.click()
        source.fill("Playwright")

        # 2. Ctrl + A (выделить всё)
        source.press("Control+A")

        # 3. Ctrl + C (копировать)
        source.press("Control+C")

        # 4. Вставка в другое поле
        target.click()
        target.press("Control+V")

        # 5. Проверка
        expect(target).to_have_value("Playwright")

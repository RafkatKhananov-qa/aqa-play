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


def test_28_03():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://demoqa.com/checkbox")
        open_button = page.locator("//span[@class='rc-tree-switcher rc-tree-switcher_close']")
        open_button.click()
        open_desktop_button = page.locator(
            "//div[@class='rc-tree-treenode rc-tree-treenode-switcher-close'][1]/span[2]")
        open_desktop_button.click()


def test_28_04():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://demoqa.com/webtables")
        table_rows = page.locator("//tbody/tr")
        expect(table_rows).to_have_count(3)
        third_table_row = page.locator("//tr[td[text()='29']]")
        cell = third_table_row.locator("xpath=./td[1]")
        expect(cell).to_have_text("Kierra")


def test_28_05():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
        add_element_button = page.locator("//button[text()='Add Element']")
        add_element_button.click(click_count=3)
        delete_buttons = page.locator("//button[@class='added-manually']")
        expect(delete_buttons).to_have_count(3)
        delete_button = page.locator("//button[@class='added-manually'][1]")
        delete_button.click()
        expect(delete_buttons).to_have_count(2)


def test_28_06():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://playwright.dev/python/")
        docs_link = page.locator("//a[text()='Docs']")
        docs_link.click()
        assert "/docs/" in page.url
        expect(page.locator("//h1")).to_have_text("Installation")

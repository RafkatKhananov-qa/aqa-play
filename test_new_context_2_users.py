from playwright.sync_api import expect


def test_save_user1(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.get_by_role("button", name="Login").click()
    page.context.storage_state(path="user1.json")


def test_save_user2(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "problem_user")
    page.fill("#password", "secret_sauce")
    page.get_by_role("button", name="Login").click()
    page.context.storage_state(path="user2.json")


def test_two_users(browser):
    # 🔹 user1 (уже залогинен)
    context1 = browser.new_context(storage_state="user1.json")
    page1 = context1.new_page()
    page1.goto("https://www.saucedemo.com/inventory.html")

    # 🔹 user2 (уже залогинен)
    context2 = browser.new_context(storage_state="user2.json")
    page2 = context2.new_page()
    page2.goto("https://www.saucedemo.com/inventory.html")

    # 🔥 проверки
    expect(page1.locator(".inventory_list")).to_be_visible()
    expect(page2.locator(".inventory_list")).to_be_visible()

    context1.close()
    context2.close()

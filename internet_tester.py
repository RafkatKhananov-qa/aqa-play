from playwright.sync_api import sync_playwright
import time


def navigate_to_example(example_name: str):
    page.locator(f"text={example_name}").click()
    return page.url


if __name__ == "__main__":
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/")
        time.sleep(5)
        heading = page.locator("h1.heading")
        title = heading.text_content()
        assert "the-internet" in title, "Не тот заголовок"
        print(f"Сайт доступен. Заголовок: {title}")
        current_url = navigate_to_example("Form Authentication")
        assert "login" in current_url, "Не тот URL"
        print(f"Перешли в: Form Authentication | URL: {current_url}")
        username = page.locator("//input[@id='username']")
        username.fill("tomsmith")
        password = page.locator("//input[@id='password']")
        password.fill("SuperSecretPassword!")
        login_button = page.locator("//button[@class='radius']")
        login_button.click()
        assert "/secure" in page.url
        print("✅ Успешный вход! URL: /login")
        logout_button = page.locator("//i//ancestor::a")
        logout_button.click()
        assert "/login" in page.url
        print(f"✅ Успешный выход! URL: {page.url}")
        browser.close()

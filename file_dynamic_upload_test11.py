from playwright.sync_api import sync_playwright, expect
import time


def navigate_to_example(example_name: str):
    page.locator(f"text={example_name}").click()
    return page.url


if __name__ == "__main__":
    with sync_playwright() as p:
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
        current_url = navigate_to_example("Dynamic Loading")
        assert "dynamic_loading" in current_url, "Не тот URL"
        print(f"Перешли в: Dynamically Loaded Page Elements | URL: {current_url}")
        example_1_link = page.locator("//a[@href='/dynamic_loading/1']")
        example_1_link.click()
        start_button = page.locator("//button[text()='Start']")
        start_button.click()
        expect(page.locator("//h4[text()='Hello World!']")).to_be_visible()
        print("✅ Элемент появился: Hello World!")

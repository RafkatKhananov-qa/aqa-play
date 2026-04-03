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
        current_url = navigate_to_example("Inputs")
        assert "inputs" in current_url, "Не тот URL"
        print(f"Перешли в: Inputs | URL: {current_url}")
        input_field = page.locator("//input")
        input_field.fill("123")
        assert input_field.input_value() == "123"
        input_field.clear()
        input_field.fill("456")
        print("✅ Введено: 456")

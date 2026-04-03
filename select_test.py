from playwright.sync_api import sync_playwright
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
        current_url = navigate_to_example("Dropdown")
        assert "dropdown" in current_url, "Не тот URL"
        print(f"Перешли в: Dropdown | URL: {current_url}")
        dropdown = page.locator("//select[@id='dropdown']")

        first_option_text = page.locator("#dropdown option").first.text_content()
        assert first_option_text == "Please select an option"

        page.locator("#dropdown").select_option("1")
        selected_text = page.locator("[selected='selected']").inner_text()
        assert selected_text == "Option 1"
        print(f"Выбрано: {selected_text}")

        page.locator("#dropdown").select_option("2")
        selected_text = page.locator("[selected='selected']").inner_text()
        assert selected_text == "Option 2"
        print(f"Выбрано: {selected_text}")

        time.sleep(5)
        browser.close()

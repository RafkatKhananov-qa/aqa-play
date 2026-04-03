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
        current_url = navigate_to_example("Checkboxes")
        assert "checkboxes" in current_url, "Не тот URL"
        print(f"Перешли в: Checkboxes | URL: {current_url}")
        checkbox_1 = page.locator("//form[@id='checkboxes']/input[@type='checkbox'][1]")
        checkbox_2 = page.locator("//form[@id='checkboxes']/input[@type='checkbox'][2]")
        assert not (checkbox_1.is_checked())
        assert (checkbox_2.is_checked())
        checkbox_1.set_checked(checked=True)
        checkbox_2.set_checked(checked=False)
        assert checkbox_1.is_checked()
        assert not (checkbox_2.is_checked())
        print("✅ Checkbox 1: checked=True")
        print("✅ Checkbox 2: checked=False")

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
        current_url = navigate_to_example("JavaScript Alerts")
        assert "javascript_alerts" in current_url, "Не тот URL"
        print(f"Перешли в: JavaScript Alerts | URL: {current_url}")
        js_alert_button = page.locator("//button[text()='Click for JS Alert']")
        js_alert_button.click()
        time.sleep(5)
        page.on("dialog", lambda dialog: dialog.accept())
        success_message_text = page.locator("//p[@id='result']")
        assert success_message_text.inner_text() == "You successfully clicked an alert"
        print("✅ Alert принят. Сообщение: You successfully clicked an alert")

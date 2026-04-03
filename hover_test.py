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
        current_url = navigate_to_example("Hovers")
        assert "hovers" in current_url, "Не тот URL"
        print(f"Перешли в: Hovers | URL: {current_url}")
        image_1 = page.locator("//div[@class='figure'][1]")
        image_1.hover()
        user_name_text = page.locator("//div[@class='figure'][1]//div[@class='figcaption']//h5")
        assert user_name_text.is_visible()
        print("✅ Навели на изображение. Текст: name: user1")

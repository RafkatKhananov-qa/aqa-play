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
        current_url = navigate_to_example("File Upload")
        assert "upload" in current_url, "Не тот URL"
        print(f"Перешли в: File Uploader | URL: {current_url}")
        file_upload_input = page.locator("//input[@id='file-upload']")
        file_upload_input.set_input_files("test_upload.txt")
        upload_button = page.locator("//input[@id='file-submit']")
        upload_button.click()
        file = page.locator("//div[@id='uploaded-files']")
        print(file.text_content())
        assert file.text_content().strip() == "test_upload.txt"
        print("✅ Файл загружен: test_upload.txt")

import re
from pathlib import Path

from playwright.sync_api import sync_playwright, expect
import time


def test_29_01_load():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        start = time.time()
        page.goto("https://the-internet.herokuapp.com/")
        page.wait_for_load_state("load")
        end = time.time()

        print("load time:", end - start)

        expect(page.get_by_role("heading", name="Welcome to the-internet")).to_be_visible()


def test_29_01_domcontentloaded():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        start = time.time()
        page.goto("https://the-internet.herokuapp.com/")
        page.wait_for_load_state("domcontentloaded")
        end = time.time()

        print("domcontentloaded time:", end - start)

        expect(page.get_by_role("heading", name="Welcome to the-internet")).to_be_visible()


def test_29_02():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
        start_button = page.locator("//button[text()='Start']")
        start_button.click()
        page.wait_for_selector("#finish", state="visible")
        expect(page.locator("//h4[text()='Hello World!']")).to_be_visible()


def test_29_03():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
        start_button = page.locator("//button[text()='Start']")
        start_button.click()
        start = time.time()
        page.wait_for_selector("#loading", state="hidden")
        expect(page.locator("//h4[text()='Hello World!']")).to_be_visible()
        end = time.time()

        print("load time:", end - start)


def test_29_04_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")
        username_input = page.locator("#username")
        username_input.fill("tomsmith")
        password_input = page.locator("#password")
        password_input.fill("SuperSecretPassword!")
        login_button = page.locator("//button[@type='submit']")
        login_button.click()
        page.wait_for_url("https://the-internet.herokuapp.com/secure")
        expect(page.get_by_text("You logged into a secure area!")).to_be_visible()


def test_29_04_fail():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")
        username_input = page.locator("#username")
        username_input.fill("tomsmith")
        password_input = page.locator("#password")
        password_input.fill("SuperSecretPassword!d")
        login_button = page.locator("//button[@type='submit']")
        login_button.click()
        try:
            page.wait_for_url("https://the-internet.herokuapp.com/secure", wait_until="domcontentloaded", timeout=3000)
        except TimeoutError:
            expect(page.locator("#flash")).to_contain_text("Your password is invalid!")


def test_29_05():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com/user/123")
        page.wait_for_url(re.compile(r"/user/\d+"))
        assert re.search(r"/user/\d+", page.url)
        print(page.url)


def test_29_06():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")

        # 2. Устанавливаем window.testReady = false
        page.evaluate("window.testReady = false")

        # 3. Через setTimeout делаем true через 2 секунды
        page.evaluate("""
                setTimeout(() => {
                    window.testReady = true;
                }, 2000);
            """)

        print("⏳ Ждём изменения состояния...")

        # 4. Ждём через wait_for_function
        page.wait_for_function("() => window.testReady === true")

        # 5. Проверка
        result = page.evaluate("window.testReady")
        assert result is True, "testReady не стал true"

        print("✅ Ожидание сработало! testReady = True")


def test_29_07():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/download")
        download = page.wait_for_event("download", timeout=5000)
        page.locator("//a[text()='some-file.txt']").click()
        download_path = Path("downloads")
        download_path.mkdir(exist_ok=True)

        file_path = download_path / download.suggested_filename
        download.save_as(file_path)

        # 4. Проверка
        assert file_path.exists(), "Файл не скачался"




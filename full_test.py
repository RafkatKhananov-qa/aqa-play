from playwright.sync_api import sync_playwright
import time


def navigate_to_example(example_name: str):
    page.locator(f"text={example_name}").click()
    return page.url


if __name__ == "__main__":
    results = {
        "Form Authentication": False,
        "Checkboxes": False,
        "Dropdown": False,
        "Inputs": False,
        "Hovers": False,
    }

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
        page.screenshot(path="screenshots/screenshot1.png")
        results["Form Authentication"] = True

        page.goto("https://the-internet.herokuapp.com/checkboxes")
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
        page.screenshot(path="screenshots/screenshot2.png")
        results["Checkboxes"] = True

        page.goto("https://the-internet.herokuapp.com/dropdown")
        dropdown = page.locator("//select[@id='dropdown']")

        first_option_text = page.locator("#dropdown option").first.text_content()
        assert first_option_text == "Please select an option"

        page.select_option("#dropdown", value="2")
        selected_text = page.locator("#dropdown option:checked").text_content()
        assert selected_text == "Option 2"
        print(f"Выбрано: {selected_text}")
        page.screenshot(path="screenshots/screenshot3.png")
        results["Dropdown"] = True

        page.goto("https://the-internet.herokuapp.com/inputs")
        input_field = page.locator("//input")
        input_field.fill("999")
        assert input_field.input_value() == "999"
        print("✅ Введено: 999")
        page.screenshot(path="screenshots/screenshot4.png")
        results["Inputs"] = True

        page.goto("https://the-internet.herokuapp.com/hovers")
        image_1 = page.locator("//div[@class='figure'][1]")
        image_1.hover()
        user_name_text = page.locator("//div[@class='figure'][1]//div[@class='figcaption']//h5")
        assert user_name_text.is_visible()
        print("✅ Навели на изображение. Текст: name: user1")
        page.screenshot(path="screenshots/screenshot5.png")
        results["Hovers"] = True

        browser.close()

        print("\n📊 ОТЧЁТ:")
        all_passed = True

        for section, status in results.items():
            if status:
                print(f"✅ {section}")
            else:
                print(f"❌ {section}")
                all_passed = False

        if all_passed:
            print("\nВсе тесты пройдены!")
        else:
            print("\nЕсть упавшие тесты.")

        print("\nСловарь результатов:")
        print(results)

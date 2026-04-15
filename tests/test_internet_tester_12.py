from pathlib import Path
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.checkboxes_page import CheckboxesPage
from pages.dropdown_page import DropdownPage
from pages.inputs_page import InputsPage
from pages.hovers_page import HoversPage


def make_screenshot(page, file_name: str):
    screenshots_dir = Path("../l26 Internet Tester/screenshots")
    screenshots_dir.mkdir(exist_ok=True)
    page.screenshot(path=screenshots_dir / file_name, full_page=True)


def run_full_test():
    results = {
        "Form Authentication": False,
        "Checkboxes": False,
        "Dropdown": False,
        "Inputs": False,
        "Hovers": False,
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        login_page = LoginPage(page)
        checkboxes_page = CheckboxesPage(page)
        dropdown_page = DropdownPage(page)
        inputs_page = InputsPage(page)
        hovers_page = HoversPage(page)

        try:
            login_page.open()
            login_page.login("tomsmith", "SuperSecretPassword!")
            login_page.verify_login_success()
            print("✅ Успешный вход! URL: /secure")

            login_page.logout()
            login_page.verify_logout_success()
            print("✅ Успешный выход! URL: /login")

            make_screenshot(page, "screenshot1.png")
            results["Form Authentication"] = True
        except Exception as e:
            print(f"❌ Form Authentication: {e}")

        try:
            checkboxes_page.open()
            checkboxes_page.set_checkboxes()
            checkboxes_page.verify_final_state()
            print("✅ Checkbox 1: checked=True")
            print("✅ Checkbox 2: checked=False")

            make_screenshot(page, "screenshot2.png")
            results["Checkboxes"] = True
        except Exception as e:
            print(f"❌ Checkboxes: {e}")

        try:
            dropdown_page.open()
            dropdown_page.verify_first_option()
            dropdown_page.select_option_2()
            dropdown_page.verify_selected("Option 2")
            print("✅ Выбрано: Option 2")

            make_screenshot(page, "screenshot3.png")
            results["Dropdown"] = True
        except Exception as e:
            print(f"❌ Dropdown: {e}")

        try:
            inputs_page.open()
            inputs_page.enter_value("999")
            inputs_page.verify_value("999")
            print("✅ Введено: 999")

            make_screenshot(page, "screenshot4.png")
            results["Inputs"] = True
        except Exception as e:
            print(f"❌ Inputs: {e}")

        try:
            hovers_page.open()
            hovers_page.hover_first_image()
            hovers_page.verify_first_user_visible()
            print("✅ Навели на изображение. Текст: name: user1")

            make_screenshot(page, "screenshot5.png")
            results["Hovers"] = True
        except Exception as e:
            print(f"❌ Hovers: {e}")

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


if __name__ == "__main__":
    run_full_test()


def test_full_test():
    run_full_test()

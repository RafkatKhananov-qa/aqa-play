import time
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from pages.checkboxes_page import CheckboxesPage
from pages.dropdown_page import DropdownPage
from pages.inputs_page import InputsPage
from pages.hovers_page import HoversPage
from pages.javascript_alert_page import AlertsPage
from pages.upload_page import UploadPage
from pages.dynamic_loading_page import DynamicLoadingPage

TITLE = "the-internet"
TITLE_FORM_AUTH = "Form Authentication"
TITLE_DROPDOWN = "Dropdown"

PAGE_LOGIN = "/login"


def test_01(page):
    page.goto("https://the-internet.herokuapp.com/")
    heading = page.locator("h1.heading")
    title = heading.text_content()
    assert "the-internet" in title, "Не тот заголовок"
    print(f"Сайт доступен. Заголовок: {title}")


def test_02(page):
    page.goto("https://the-internet.herokuapp.com/")

    base_page = BasePage(page)
    base_page.navigate_to_example("Form Authentication")

    time.sleep(5)

    assert "login" in page.url, "Не тот URL"


def test_03(page):
    page.goto("https://the-internet.herokuapp.com/")

    login_page = LoginPage(page)
    login_page.login_process()

    login_page.assert_text_in_url_print("/secure", "✅ Успешный вход! ")


def test_04(page):
    page.goto("https://the-internet.herokuapp.com/")

    login_page = LoginPage(page)
    login_page.login_process()

    login_page.assert_text_in_url_print("/secure", "✅ Успешный вход! ")

    secure_page = SecurePage(page)
    secure_page.click_logout()

    login_page.assert_text_in_url_print("/login", "✅ Успешный выход! URL: /login ")


def test_05(page):
    checkboxes_page = CheckboxesPage(page)

    checkboxes_page.open()
    checkboxes_page.verify_initial_state()
    checkboxes_page.set_checkboxes()
    checkboxes_page.verify_final_state()
    checkboxes_page.print_result()


def test_06(page):
    dropdown_page = DropdownPage(page)

    dropdown_page.open()
    dropdown_page.verify_first_option()

    dropdown_page.select_option_1()
    dropdown_page.verify_selected("Option 1")

    dropdown_page.select_option_2()
    dropdown_page.verify_selected("Option 2")


def test_07(page):
    inputs_page = InputsPage(page)

    inputs_page.open()

    inputs_page.enter_value("123")
    inputs_page.verify_value("123")

    inputs_page.clear_input()
    inputs_page.enter_value("456")

    inputs_page.verify_value("456")
    inputs_page.print_result("456")


def test_08(page):
    hovers_page = HoversPage(page)

    hovers_page.open()
    hovers_page.hover_first_image()
    hovers_page.verify_first_user_visible()
    hovers_page.print_result()


def test_09(page):
    alerts_page = AlertsPage(page)

    alerts_page.open()
    alerts_page.accept_js_alert()
    alerts_page.verify_success_message()
    alerts_page.print_result()


def test_10(page):
    upload_page = UploadPage(page)

    upload_page.open()
    upload_page.upload_file()
    upload_page.submit()

    upload_page.verify_uploaded_file("test_upload.txt")
    upload_page.print_result()


def test_11(page):
    dynamic_page = DynamicLoadingPage(page)

    dynamic_page.open()
    dynamic_page.open_example_1()
    dynamic_page.click_start()
    dynamic_page.wait_for_hello_text()
    dynamic_page.print_result()

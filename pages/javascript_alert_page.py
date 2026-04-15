from pages.base_page import BasePage


class AlertsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.js_alert_button = page.locator("text=Click for JS Alert")
        self.result_text = page.locator("#result")

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    def accept_js_alert(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.js_alert_button.click()

    def get_result_text(self):
        return self.result_text.text_content().strip()

    def verify_success_message(self):
        actual = self.get_result_text()
        assert actual == "You successfully clicked an alert", \
            f"Ожидалось сообщение об успехе, получено: {actual}"

    def print_result(self):
        print(f"✅ Alert обработан. Текст: {self.get_result_text()}")

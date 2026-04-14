from pages.base_page import BasePage


class InputsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        # локатор
        self.input_field = page.locator("input")

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/inputs")

    def enter_value(self, value):
        self.input_field.fill(value)

    def clear_input(self):
        self.input_field.clear()

    def get_value(self):
        return self.input_field.input_value()

    def verify_value(self, expected):
        actual = self.get_value()
        assert actual == expected, f"Ожидалось {expected}, получено {actual}"

    def print_result(self, value):
        print(f"✅ Введено: {value}")

from pages.base_page import BasePage


class DropdownPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        # локаторы
        self.dropdown = page.locator("#dropdown")
        self.options = page.locator("#dropdown option")

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/dropdown")

    def verify_first_option(self):
        first_option_text = self.options.first.text_content().strip()
        assert first_option_text == "Please select an option"

    def select_option_1(self):
        self.dropdown.select_option("1")

    def select_option_2(self):
        self.dropdown.select_option("2")

    def get_selected_text(self):
        return self.page.locator("#dropdown option:checked").text_content().strip()

    def verify_selected(self, expected_text):
        selected_text = self.get_selected_text()
        assert selected_text == expected_text, f"Ожидалось {expected_text}, получено {selected_text}"
        print(f"✅ Выбрано: {selected_text}")

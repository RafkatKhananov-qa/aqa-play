from pages.base_page import BasePage


class CheckboxesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        # локаторы
        self.checkbox_1 = page.locator("//form[@id='checkboxes']/input[@type='checkbox'][1]")
        self.checkbox_2 = page.locator("//form[@id='checkboxes']/input[@type='checkbox'][2]")

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/checkboxes")

    def verify_initial_state(self):
        assert not self.checkbox_1.is_checked(), "Checkbox 1 должен быть не отмечен"
        assert self.checkbox_2.is_checked(), "Checkbox 2 должен быть отмечен"

    def set_checkboxes(self):
        self.checkbox_1.set_checked(True)
        self.checkbox_2.set_checked(False)

    def verify_final_state(self):
        assert self.checkbox_1.is_checked(), "Checkbox 1 должен быть отмечен"
        assert not self.checkbox_2.is_checked(), "Checkbox 2 должен быть снят"

    def print_result(self):
        print("✅ Checkbox 1: checked=True")
        print("✅ Checkbox 2: checked=False")

from pages.base_page import BasePage


class HoversPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        # локаторы
        self.figures = page.locator(".figure")

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/hovers")

    def hover_first_image(self):
        self.figures.nth(0).hover()

    def get_first_user_text(self):
        return self.figures.nth(0).locator(".figcaption h5").text_content().strip()

    def verify_first_user_visible(self):
        caption = self.figures.nth(0).locator(".figcaption")
        assert caption.is_visible(), "Текст не появился"

    def print_result(self):
        text = self.get_first_user_text()
        print(f"✅ Навели на изображение. Текст: {text}")

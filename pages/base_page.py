class BasePage:

    def __init__(self, page):
        self.page = page

    def navigate_to_example(self, example_name: str):
        self.page.locator(f"text={example_name}").click()

    def assert_text_in_url_print(self, text_expected: str, msg: str = ""):
        assert text_expected in self.page.url, "Не та страница!"
        print(f"\n{msg}URL: {self.page.url}")

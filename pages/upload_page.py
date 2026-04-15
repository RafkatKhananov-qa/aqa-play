from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_FILE = BASE_DIR / "test_data" / "test_upload.txt"


class UploadPage:
    def __init__(self, page):
        self.page = page

        self.file_input = page.locator("#file-upload")
        self.upload_button = page.locator("#file-submit")
        self.uploaded_file = page.locator("#uploaded-files")

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/upload")

    def upload_file(self, file_path: Path = DEFAULT_FILE):
        self.file_input.set_input_files(file_path)

    def submit(self):
        self.upload_button.click()

    def get_uploaded_filename(self):
        return self.uploaded_file.text_content().strip()

    def verify_uploaded_file(self, expected_name: str):
        actual = self.get_uploaded_filename()
        assert actual == expected_name, f"Ожидалось {expected_name}, получено {actual}"

    def print_result(self):
        print(f"✅ Файл загружен: {self.get_uploaded_filename()}")

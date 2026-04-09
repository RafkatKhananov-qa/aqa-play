from playwright.sync_api import sync_playwright, expect
import re


def test_text_1():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://demoqa.com/buttons")
        double_click_me_btn_text = page.locator("#doubleClickBtn").inner_text()
        assert double_click_me_btn_text == "Double Click Me"


def test_text_2():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://demoqa.com/buttons")
        click_me_btn = page.locator("//button[text()='Click Me']")
        click_me_btn.click()
        pop_up_text = page.locator("#dynamicClickMessage")
        expect(pop_up_text).to_have_text("You have done a dynamic click")


def test_text_3():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://demoqa.com/text-box")
        full_name_input = page.locator("#userName")
        full_name_input.fill("Rafkat")
        email_input = page.locator("#userEmail")
        email_input.fill("bob123@mail.ru")
        print(f"Имя: {full_name_input.input_value()}, Email: {email_input.input_value()}")


def test_text_4():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://demoqa.com/select-menu")
        options = page.locator("#oldSelectMenu option")
        texts = options.all_inner_texts()
        print(texts)
        assert "Blue" in texts


def test_text_5():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://demoqa.com/text-box")
        current_address_label = page.locator("#currentAddress-label")
        inner = current_address_label.inner_text()
        text = current_address_label.text_content()

        # вывод через repr()
        print("inner_text():", repr(inner))
        print("text_content():", repr(text))

        # сравнение
        assert inner == text


def test_text_6():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/")
        expect(page.locator("//h2")).to_contain_text("Available Examples")


def test_text_7():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")
        username_input = page.locator("#username")
        username_input.fill("tomsmith")
        password_input = page.locator("#password")
        password_input.fill("4654654")
        login_button = page.locator("//button[@type='submit']")
        login_button.click()
        expect(page.locator("#flash")).to_contain_text("Your password is invalid!")


def test_text_8():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")
        username_input = page.locator("#username")
        username_input.fill("tomsmith")
        password_input = page.locator("#password")
        password_input.fill("SuperSecretPassword!")
        login_button = page.locator("//button[@type='submit']")
        login_button.click()
        assert "/secure" in page.url
        success_login_text = page.locator("#flash").inner_text()
        assert "You logged into a secure area!" in success_login_text
        # logout_button = page.locator("//a[@href='/logout']")
        # print(logout_button.input_value())


def test_text_9():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/checkboxes")
        checkboxes = page.locator("//input[@type='checkbox']")
        count = checkboxes.count()

        states = []
        for i in range(count):
            checkbox = checkboxes.nth(i)
            state = "checked" if checkbox.is_checked() else "unchecked"
            states.append(state)

        block_text = page.locator("#checkboxes").inner_text()
        print("Текст блока:", repr(block_text))

        print(f"Количество чекбоксов: {count}")
        for i, state in enumerate(states, start=1):
            print(f"Checkbox {i}: {state}")


def test_text_10():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
        start_button = page.locator("//button")
        start_button.click()
        expect(page.locator("//h4[text()='Hello World!']")).to_have_text("Hello World!")
        text = page.locator("//h4[text()='Hello World!']").inner_text()
        assert text == "Hello World!"


def test_text_11():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/iframe")
        paragraph_text = page.frame_locator("#mce_0_ifr"
                                            ).locator("//p[text()='Your content goes here.']"
                                                      ).inner_text()
        assert "Your content goes here" in paragraph_text
        print(paragraph_text)


def test_text_12():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://www.urn.su/ui/basic_test/#intro")
        title = page.locator("//h1")
        title_text = title.inner_text()
        print(title_text)
        assert title_text.strip() != ""


def test_text_13():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://www.urn.su/ui/basic_test/#intro")

        # 1. находим все элементы списков
        items = page.locator("ul li, ol li")

        # 2. получаем тексты всех элементов
        texts = items.all_inner_texts()

        # 3. выводим количество и сами элементы
        print("Количество элементов списка:", len(texts))
        print("Элементы списка:")
        for i, text in enumerate(texts, start=1):
            print(f"{i}. {repr(text)}")

        # 4. проверяем первый элемент
        assert len(texts) > 0, "На странице не найдено элементов списка"
        assert "Введение" in texts[0], f"Ожидался текст 'Введение', получено: {texts[0]}"


def test_text_14():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://www.urn.su/ui/basic_test/#intro")
        text = page.locator("//main/p[@class='p2'][1]")
        text_value_1 = text.inner_text()
        text_value_2 = text.text_content()

        print("inner_text():", repr(text_value_1))
        print("text_content():", repr(text_value_2))

        print(text_value_1 == text_value_2)

        print("inner_text().strip():", repr(text_value_1.strip()))
        print("text_content().strip():", repr(text_value_2.strip()))


def test_text_15():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://www.urn.su/ui/basic_test/#intro")

        candidates = page.locator("div, p, li, td, label, a, span")
        count = candidates.count()

        for i in range(count):
            el = candidates.nth(i)

            try:
                inner = el.inner_text()
                content = el.text_content()

                if content is None:
                    continue

                if inner.strip() or content.strip():
                    if inner != content:
                        print(f"Элемент #{i}")
                        print("inner_text():", repr(inner))
                        print("text_content():", repr(content))
                        print("len(inner):", len(inner), "len(content):", len(content))
                        print("-" * 50)
            except Exception:
                continue


def test_bonus_task():
    with (sync_playwright() as p):
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto("https://volna.tj/")
        expect(page.locator("//div[@class='product-cat-price-payment' "
                            "and text()='от 3671с/мес']")).to_have_text(re.compile(r"от\s\d+с/мес"))
        text = page.locator("//div[@class='product-cat-price-payment' "
                            "and text()='от 3671с/мес']").inner_text()
        print(text)

        match = re.search(r"\d+", text)
        assert match is not None, "Число в тексте не найдено"

        value = int(match.group())
        print("Число:", value)

        assert value > 0, "Значение должно быть больше 0"

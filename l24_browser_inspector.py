from datetime import datetime
import sys
from pathlib import Path
import re
import json
import argparse
import time
from importlib.metadata import version
import playwright
from playwright.sync_api import sync_playwright


def inspect_page(url: str,
                 browser_type: str = "chromium",
                 headless: bool = True,
                 screenshot: bool = False,
                 retries: int = 1) -> dict:
    with sync_playwright() as p:
        for attempt in range(1, retries + 1):
            browser = None
            page = None

            try:

                if browser_type == "chromium":
                    browser = p.chromium.launch(headless=headless)
                elif browser_type == "firefox":
                    browser = p.firefox.launch(headless=headless)
                elif browser_type == "webkit":
                    browser = p.webkit.launch(headless=headless)
                else:
                    raise ValueError(f"Unsupported browser: {browser_type}")

                page = browser.new_page()
                start = time.perf_counter()
                response = page.goto(url)
                title = page.title()
                load_time = round(time.perf_counter() - start, 2)

                result = {
                    "url": url,
                    "browser": browser_type,
                    "title": title,
                    "success": True,
                    "viewport": page.viewport_size,
                    "url_final": page.url,
                    "status": response.status if response else None,
                    "load_time_sec": float(load_time)
                }

                if screenshot:
                    screenshots_dir = Path("output/screenshots")
                    screenshots_dir.mkdir(parents=True, exist_ok=True)

                    safe_name = re.sub(r'[^\w\-_]', '_', url)
                    screenshot_path = screenshots_dir / f"{browser_type}_{safe_name}.png"

                    page.screenshot(path=str(screenshot_path))
                    result["screenshot"] = str(screenshot_path)

                return result

            except Exception as e:
                print(f"❌ Ошибка: {e}")

                if attempt < retries:
                    if page is not None:
                        page.wait_for_timeout(1000)
                    continue

                return {
                    "url": url,
                    "browser": browser_type,
                    "success": False,
                    "error": str(e)
                }

            finally:
                if browser is not None:
                    browser.close()


def inspect_batch(urls: list[str],
                  browsers: list[str] = ["chromium"],
                  **kwargs) -> list[dict]:
    results = []

    for url in urls:
        for browser in browsers:
            result = inspect_page(url, browser_type=browser, **kwargs)
            results.append(result)

    return results


def save_report(results: list[dict], output_file: str) -> str:
    reports_dir = Path("output/reports")
    reports_dir.mkdir(parents=True, exist_ok=True)

    # имя файла (например report.json)
    output_path = reports_dir / Path(output_file).name

    report_data = {
        "generated_at": datetime.now().isoformat(),
        "total_urls": len({r["url"] for r in results}),
        "meta": {
            "playwright_version": version("playwright"),
            "python_version": sys.version
        },
        "results": results
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=4)

    return str(output_path)


def inspect_with_session(url: str,
                         user_dir: str = "session_data") -> dict:
    with sync_playwright() as p:
        context = None
        page = None

        try:
            user_data_path = Path(user_dir)
            user_data_path.mkdir(parents=True, exist_ok=True)

            context = p.chromium.launch_persistent_context(
                user_data_dir=str(user_data_path),
                headless=True
            )

            page = context.new_page()
            response = page.goto(url, wait_until="load")

            existing_marker = page.evaluate("localStorage.getItem('inspector_run')")

            result = {
                "url": url,
                "browser": "chromium",
                "title": page.title(),
                "success": True,
                "viewport": page.viewport_size or "default",
                "url_final": page.url,
                "status": response.status if response else None
            }

            if existing_marker is not None:
                result["session_marker"] = existing_marker

            page.evaluate("localStorage.setItem('inspector_run', '1')")

            return result

        except Exception as e:
            print(f"❌ Ошибка: {e}")

            return {
                "url": url,
                "browser": "chromium",
                "success": False,
                "error": str(e)
            }

        finally:
            if context is not None:
                context.close()


# if __name__ == "__main__":
#     result = inspect_page(
#         "https://example.com",
#         screenshot=True,
#         retries=3
#     )
#     print(f"[{result['browser']}] {result['title']}")
#     print(f"Viewport: {result['viewport']}")
#     print(f"Финальный URL: {result['url_final']}")
#     print(f"⏱️ Загрузка: {result['load_time_sec']}с")
#
#     if "screenshot" in result:
#         print(f"📸 Скриншот: {result['screenshot']}")

# if __name__ == "__main__":
#     urls = ["https://example.com", "https://httpbin.org"]
#     results = inspect_batch(
#         urls,
#         browsers=["chromium", "firefox"],
#         screenshot=True
#     )
#
#     for r in results:
#         if r["success"]:
#             print(f"✅ [{r['browser']}] {r['url']} | {r['title']}")
#             if "screenshot" in r:
#                 print(f"📸 Скриншот: {r['screenshot']}")
#         else:
#             print(f"❌ [{r['browser']}] {r['url']} | {r['error']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Browser Inspector")

    parser.add_argument(
        "urls",
        nargs="+",
        help="Один или несколько URL для проверки"
    )

    parser.add_argument(
        "--browsers",
        nargs="+",
        default=["chromium"],
        help="Список браузеров: chromium firefox webkit"
    )

    parser.add_argument(
        "--headless",
        action="store_true",
        help="Запускать браузер в headless режиме"
    )

    parser.add_argument(
        "--screenshot",
        action="store_true",
        help="Сохранять скриншоты"
    )

    parser.add_argument(
        "--retries",
        type=int,
        default=1,
        help="Количество попыток при ошибке"
    )

    parser.add_argument(
        "--output",
        type=str,
        help="Путь к JSON-отчёту"
    )

    args = parser.parse_args()

    results = inspect_batch(
        urls=args.urls,
        browsers=args.browsers,
        headless=args.headless,
        screenshot=args.screenshot,
        retries=args.retries
    )

    for r in results:
        if r["success"]:
            print(f"✅ [{r['browser']}] {r['url']} | {r['title']}")
            if "screenshot" in r:
                print(f"📸 Скриншот: {r['screenshot']}")
        else:
            print(f"❌ [{r['browser']}] {r['url']} | {r['error']}")

    if args.output:
        path = save_report(results, args.output)
        print(f"Отчёт сохранён: {path}")

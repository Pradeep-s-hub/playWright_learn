import re
import time
from playwright.sync_api import sync_playwright,expect
def test_google_title(page):
    page.goto("https://www.google.com/ncr")
    try:
        time.sleep(2)
        page.get_by_role("button", name="Try it").click(timeout=3000)
    except:
        print("No cookie consent button found.")
        assert False
        
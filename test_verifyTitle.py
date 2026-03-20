from playwright.sync_api import Page, expect
def test_verify_title(page: Page):
    page.goto("https://www.google.com/")
    expect(page).to_have_title("Google")
def test_verify_title_gettingIT(page: Page):
    page.goto("https://www.google.com/")
    Current_title = page.title()   
    print("Current Title:", Current_title)
    expect(page).to_have_title(Current_title)
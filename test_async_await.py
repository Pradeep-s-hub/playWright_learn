import pytest
from playwright.async_api import Page, async_playwright, expect
#pip install pytest-asyncio

@pytest.mark.asyncio
async def test_verify_page_url_gettingIT(page: Page):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.google.com/")
        Current_url = await page.url()   
        print("Current URL:", Current_url)
        await expect(page).to_have_url(Current_url) 
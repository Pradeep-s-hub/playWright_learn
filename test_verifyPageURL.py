#playwright provide a built-in fixture called "page" that allows you to interact with web pages in your tests.
# from playwrite we have snc_api and async_api.
from playwright.sync_api import Page, expect
def test_verify_page_url(page: Page):
    #by default playwrite will open in chromium browser but we can also specify the browser we want to use.
    page.goto("https://www.google.com/")
    expect(page).to_have_url("https://www.google.com/")
def test_verify_page_url_gettingIT(page: Page):
    page.goto("https://www.google.com/")
    Current_url = page.url()   
    print("Current URL:", Current_url)
    expect(page).to_have_url(Current_url) 
    
# there are two modes of ececution in playwrite one is headless and other is headed mode. 
# by default it will run in headless mode  we can also specify the mode we want to run in.
#hedless mode is faster than headed mode because it does not have to render the UI but it is not visible to the user.
#(playwriteEnv) D:\software\playWritePro>pytest Test_playWrite/test_verifyPageURL.py -v -s 
#================================================================ test session starts ================================================================
#platform win32 -- Python 3.12.12, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\PRADEEP\anaconda3\envs\playwriteEnv\python.exe
#cachedir: .pytest_cache
#rootdir: D:\software\playWritePro
#plugins: base-url-2.1.0, playwright-0.7.2
#collected 1 item
#
#Test_playWrite/test_verifyPageURL.py::test_verify_page_url[chromium] PASSED
#
#================================================================= 1 passed in 6.92s ================================================================= 
#
#(playwriteEnv) D:\software\playWritePro>

#headed mode is slower than headless mode because it has to render the UI but it is visible to the user.
#(playwriteEnv) D:\software\playWritePro>pytest Test_playWrite/test_verifyPageURL.py -v -s --headed
#================================================================ test session starts ================================================================
#platform win32 -- Python 3.12.12, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\PRADEEP\anaconda3\envs\playwriteEnv\python.exe
#cachedir: .pytest_cache
#rootdir: D:\software\playWritePro
#plugins: base-url-2.1.0, playwright-0.7.2
#collected 1 item
#
#Test_playWrite/test_verifyPageURL.py::test_verify_page_url[chromium] PASSED
#
#================================================================= 1 passed in 4.07s ================================================================= 
#
#(playwriteEnv) D:\software\playWritePro>
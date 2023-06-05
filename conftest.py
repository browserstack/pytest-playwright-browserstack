import pytest
from browserstack.local import Local
from jsonmerge import merge
from dotenv import load_dotenv

from playwright.sync_api import Playwright

load_dotenv()

@pytest.fixture(scope='session')
def session_capabilities(playwright: Playwright):
    browser = playwright.chromium.launch(channel='chrome', headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

@pytest.fixture(scope='session')
def base_url():
    return "https://bstackdemo.com/"

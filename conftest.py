import threading
import urllib
import uuid
#import threading
from multiprocessing import Process, Lock
import pytest
from browserstack.local import Local
import os, json
from jsonmerge import merge
from dotenv import load_dotenv
import time

from playwright.sync_api import Playwright
from playwright.sync_api import Page

lock = Lock()
threaded_count = 0

load_dotenv()

TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0


BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY']

if os.environ.get('REMOTE', 'true') == "true":
    @pytest.fixture(scope='function')
    def session_capabilities(playwright: Playwright):
        global timenow
        global lock
        test_name = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0].split('::')[1]
        capabilities = {}
        stringifiedCaps = urllib.parse.quote(json.dumps(capabilities))
        caps = 'wss://cdp.browserstack.com/playwright?caps=' + stringifiedCaps
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        
        yield page
        context.close()
        browser.close()

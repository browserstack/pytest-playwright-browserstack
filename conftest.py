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

lock = Lock()
threaded_count = 0

load_dotenv()

CONFIG_FILE = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else 'resources/parallel.json'
TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

with open(CONFIG_FILE) as data_file:
    CONFIG = json.load(data_file)




BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] if 'BROWSERSTACK_USERNAME' in os.environ else CONFIG["user"]
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else CONFIG[
    "key"]



if os.environ['REMOTE'] == "true":
    @pytest.fixture(scope='session')
    def session_capabilities(playwright: Playwright):
        global timenow
        global lock
        test_name = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0].split('::')[1]
        capabilities = merge(CONFIG['environments'][TASK_ID], CONFIG["capabilities"])
        print(str(capabilities))
        capabilities['browserstack.username'] = BROWSERSTACK_USERNAME
        capabilities['browserstack.accessKey'] = BROWSERSTACK_ACCESS_KEY
        capabilities['source'] = 'pytest:sample-main:v1.0'
        capabilities['sessionName'] = test_name
        print(CONFIG['base_url'])
        if "local" in capabilities and capabilities['local']:
            capabilities['browserstack.local'] = "true"
        print("capabilities => " + json.dumps(capabilities))
        stringifiedCaps = urllib.parse.quote(json.dumps(capabilities))
        caps = 'wss://cdp.browserstack.com/playwright?caps=' + stringifiedCaps
        browser = playwright.chromium.connect(str(caps))
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
else:
    @pytest.fixture(scope='session')
    def session_capabilities(playwright: Playwright):
        capabilities = CONFIG['environments'][TASK_ID]
        if "browser" in capabilities and capabilities['browser'] == 'chrome':
            browser = playwright.chromium.launch(channel='chrome', headless=False)
        if "browser" in capabilities and capabilities['browser'] == 'edge':
            browser = playwright.chromium.launch(channel='msedge', headless=False)
        elif "browser" in capabilities and capabilities['browser'] == 'firefox':
            browser = playwright.firefox.launch(headless=False)
        else:
            browser = playwright.webkit.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture(scope='session')
def base_url():
    print(CONFIG['base_url'])
    return CONFIG['base_url']


#def pytest_sessionfinish(session, exitstatus):
#    stop_local()

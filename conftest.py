import urllib


import pytest
from browserstack.local import Local
import os, json
from jsonmerge import merge
from dotenv import load_dotenv
import time

from playwright.sync_api import Playwright

load_dotenv()

CONFIG_FILE = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else 'resources/single.json'
TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

with open(CONFIG_FILE) as data_file:
    CONFIG = json.load(data_file)

bs_local = None
timenow = None

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] if 'BROWSERSTACK_USERNAME' in os.environ else CONFIG["user"]
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else CONFIG["key"]

def start_local():
    """Code to start browserstack local before start of test."""
    global bs_local
    global timenow
    timenow=str(time.time()*1000)
    print(timenow)
    bs_local = Local()
    bs_local_args = { "key": BROWSERSTACK_ACCESS_KEY or "access_key", "localIdentifier": timenow }
    bs_local.start(**bs_local_args)

def stop_local():
    """Code to stop browserstack local after end of test."""
    global bs_local
    if bs_local is not None:
        bs_local.stop()


if os.environ['REMOTE'] == "true":
#if "true" == "true":
  @pytest.fixture(scope='session')
  def session_capabilities(playwright: Playwright):
    global timenow
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0].split('::')[1]
    capabilities = merge(CONFIG['environments'][TASK_ID],CONFIG["capabilities"])
    capabilities['browserstack.username'] = BROWSERSTACK_USERNAME
    capabilities['browserstack.accessKey'] = BROWSERSTACK_ACCESS_KEY
    capabilities['source'] = 'pytest:sample-main:v1.0'
    capabilities['sessionName'] = test_name
    print(CONFIG['base_url'])
    if "local" in capabilities and capabilities['local']:
        start_local()
        capabilities['localIdentifier'] = timenow
    print("capabilities => "+json.dumps(capabilities))
    stringifiedCaps = urllib.parse.quote(json.dumps(capabilities))
    caps = 'wss://cdp.browserstack.com/playwright?caps=' + stringifiedCaps
    browser = playwright.chromium.connect(str(caps))
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

@pytest.fixture(scope='session')
def base_url():
  print(CONFIG['base_url'])
  return CONFIG['base_url']

def pytest_sessionfinish(session, exitstatus):
  stop_local()

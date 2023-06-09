import re

import pytest
from playwright.sync_api import expect

def test_bstack_local_sample(page) -> None:
    try:
        #Navigate to the base url
        page.goto("http://bs-local.com:45454", timeout=0)

        #Verify if BrowserStackLocal running
        print(page.title())
        assert page.title() == "BrowserStack Local"
        mark_test_status("passed", "BrowserStack local is Up & running", page)
    except Exception as err:
        #Extract error message from Exception
        error=str(err).split("Call log:")[0].replace("\n"," but ").replace(":","=>").replace("'","")
        mark_test_status("failed", error, page)
        raise ValueError(error)

def mark_test_status(status, reason, page):
    page.evaluate("_ => {}", "browserstack_executor: {\"action\": \"setSessionStatus\", \"arguments\": {\"status\":\""+ status + "\", \"reason\": \"" + reason + "\"}}")

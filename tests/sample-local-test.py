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
    except Exception as err:
        #Extract error message from Exception
        error=str(err).split("Call log:")[0].replace("\n"," but ").replace(":","=>").replace("'","")
        raise ValueError(error)

@pytest.mark.xfail()
def checkTitle(title):
    print("Title =>"+title)
    assert title() == "BrowserStack Lical"

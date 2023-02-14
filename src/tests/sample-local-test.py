import re
from playwright.sync_api import expect


def test_sample(session_capabilities,base_url) -> None:

    try:
        # Load the PAge returned by the fixture
        page=session_capabilities
        print(page)
        #Navigate to the base url
        page.goto(base_url, timeout=0)

        #Verify if BrowserStackLocal running
        print(page.title())
        expect(page).to_have_title(re.compile("BrowserStack Local"))

        #Update the test result
        mark_test_status("passed", "The title contains "+page.title()+", BrowserStack local is ip & running", page)
    except Exception as err:
        #Extract error message from Exception
        error=str(err).split("Call log:")[0].replace("\n"," but ").replace(":","=>").replace("'","")
        mark_test_status("failed", error, page)

def mark_test_status(status, reason, page):
  page.evaluate("_ => {}", "browserstack_executor: {\"action\": \"setSessionStatus\", \"arguments\": {\"status\":\""+ status + "\", \"reason\": \"" + reason + "\"}}");

def log_contextual_info(desc,loglevel,page):
    page.evaluate("_ => {}",
                  "browserstack_executor: {\"action\": \"annotate\", \"arguments\": {\"data\":\"" + desc + "\", \"level\": \"" + loglevel + "\"}}");
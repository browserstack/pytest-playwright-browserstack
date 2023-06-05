# pytest-playwright-browserstack

Playwright with PyTest Test runner Integration with BrowserStack.

![BrowserStack Logo](https://d98b8t1nnulk5.cloudfront.net/production/images/layout/logo-header.png?1469004780)
## Prerequisite
* Python3

## Setup

* Clone the repo
* Install dependencies `pip install -r requirements.txt`
* To run your automated tests using BrowserStack, you must provide a valid username and access key. This can be done by setting the BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY environment variables.

## Run sample tests
* To run tests, run `browserstack-sdk pytest -s src/tests/sample-test.py`
* To run local tests, run `browserstack-sdk pytest -s src/tests/sample-local-test.py`.

## Understand how many parallel sessions you need by using our [Parallel Test Calculator](https://www.browserstack.com/automate/parallel-calculator?ref=github)

## Notes
* You can view your test results on the [BrowserStack Automate dashboard](https://www.browserstack.com/automate)

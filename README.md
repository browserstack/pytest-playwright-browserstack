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
* To run parallel tests, run `paver run single remote`

## Run tests on locally hosted websites
* To run a local test, (if you have not set the BROWSERSTACK_ACCESS_KEY environment variable) first go to resources/local.json then edit key on line 3
* Run `paver run local remote`

## Run sample tests in parallel
* To run parallel tests, run `paver run parallel remote`


## Run sample tests locally
* To run tests locally you may have to install the browser dependencies. 
* For example, if you want to run the test on Firefox borwsoer, you have to run the below command

```
playwright install firefox	

```

* After installing the browsers, run `paver run single on-prem`


 Understand how many parallel sessions you need by using our [Parallel Test Calculator](https://www.browserstack.com/automate/parallel-calculator?ref=github)

## Notes
* You can view your test results on the [BrowserStack Automate dashboard](https://www.browserstack.com/automate)
* To test on a different set of browsers, check out our [platform configurator](https://www.browserstack.com/automate/python#setting-os-and-browser)
# pytest-playwright-browserstack

Sample project demonstrating how to run [Playwright](https://playwright.dev/python/) tests with [pytest](https://docs.pytest.org/) on [BrowserStack](https://www.browserstack.com) using the BrowserStack SDK.

## Prerequisites

- Python 3.8+
- A BrowserStack account ([sign up for free](https://www.browserstack.com/users/sign_up))

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/browserstack/pytest-playwright-browserstack.git
   cd pytest-playwright-browserstack
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   playwright install
   ```

3. Set your BrowserStack credentials in `browserstack.yml`:

   ```yaml
   userName: YOUR_USERNAME
   accessKey: YOUR_ACCESS_KEY
   ```

   Or export them as environment variables:

   ```bash
   export BROWSERSTACK_USERNAME=YOUR_USERNAME
   export BROWSERSTACK_ACCESS_KEY=YOUR_ACCESS_KEY
   ```

## Running Tests

Run the sample test on BrowserStack:

```bash
browserstack-sdk pytest -s tests/
```

This will run the Playwright tests across the platforms defined in `browserstack.yml`.

## Project Structure

```
pytest-playwright-browserstack/
├── tests/
│   └── test_sample.py          # Playwright test using page fixture
├── browserstack.yml             # BrowserStack SDK configuration
├── requirements.txt             # Python dependencies
└── README.md
```

## Configuration

Edit `browserstack.yml` to customize:

- **Platforms**: Add or change browser combinations under `platforms`
- **Parallelism**: Adjust `parallelsPerPlatform` to run more tests concurrently
- **Browsers**: Use `playwright-chromium`, `playwright-webkit`, or `playwright-firefox`
- **Debugging**: Set `debug`, `networkLogs`, or `consoleLogs` for troubleshooting

See the full list of configuration options in the [BrowserStack SDK documentation](https://www.browserstack.com/docs/automate/playwright/getting-started/python).

## How It Works

The BrowserStack Python SDK wraps test execution. When you run tests via `browserstack-sdk`, it intercepts Playwright's browser launch and routes sessions to BrowserStack's cloud via CDP (Chrome DevTools Protocol). Your tests use standard Playwright and pytest APIs with no code changes needed.

The `page` fixture is provided automatically by the `pytest-playwright` plugin — no custom `conftest.py` is required.

## Resources

- [BrowserStack Playwright Getting Started Guide](https://www.browserstack.com/docs/automate/playwright/getting-started/python)
- [Playwright for Python Documentation](https://playwright.dev/python/)
- [pytest-playwright Plugin](https://github.com/microsoft/playwright-pytest)
- [BrowserStack SDK Configuration](https://www.browserstack.com/docs/automate/selenium/sdk-config)
- [Supported Browsers and OS](https://www.browserstack.com/list-of-browsers-and-platforms/automate)

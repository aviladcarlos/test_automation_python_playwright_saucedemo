from playwright.sync_api import Playwright

import pytest

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", choices=("chrome", "firefox", "edge"),
        help="Specify browser to run locally (e.g., chrome, firefox, edge)"
    )

@pytest.fixture
def browser_instance(playwright :Playwright, request):

    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "edge":
        browser = playwright.chromium.launch(channel="msedge", headless=False)

    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

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
    tracing_option = request.config.getoption("--tracing")

    if tracing_option == "on" or "retain-on-failure":
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    yield page

    if tracing_option == "on" and hasattr(request.node, "test_failed"):
        test_name = request.path.stem
        context.tracing.stop(path=f"../test-results/{test_name}_{browser_name}_failed_trace.zip")
    elif tracing_option == "on":
        test_name = request.path.stem
        context.tracing.stop(path=f"../test-results/{test_name}_{browser_name}_trace.zip")


    if tracing_option == "retain-on-failure" and hasattr(request.node, "test_failed"):
        test_name = request.path.stem
        context.tracing.stop(path=f"../test-results/{test_name}_{browser_name}_failed_trace.zip")
    else:
        context.tracing.stop()

    context.close()
    browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        item.test_failed = True

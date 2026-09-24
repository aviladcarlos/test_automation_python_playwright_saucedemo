from pytest_bdd import given, when, then, parsers, scenarios
import pytest

from pageobjects.login_page_objects import LoginPageObjects

scenarios("../features/login_locked_out_user.feature")

@pytest.fixture
def shared_data():
    return {}

@given("a locked out user is on the login page")
def standard_user_on_landing_page(browser_instance, shared_data):
    login_page = LoginPageObjects(browser_instance)
    login_page.navigate_to_login_page()
    shared_data["login_page"] = login_page

@when(parsers.parse("the locked out user logins to Sauce Demo with {username} and {password}"))
def login_to_sauce_demo(username, password, shared_data):
    login_page = shared_data["login_page"]
    login_page.login(username, password)

@then("the locked out user should see the locked out message")
def see_products_page(shared_data):
    login_page = shared_data["login_page"]
    login_page.verify_user_locked_out_message()

@then("the locked out user should remain on the login page after locked out message is displayed")
def verify_still_on_login_page(shared_data):
    login_page = shared_data["login_page"]
    login_page.verify_login_box_visible()

from pytest_bdd import given, when, then, parsers, scenarios
import pytest

from pageobjects.login_page_objects import LoginPageObjects

scenarios("../features/login_standard_user.feature")

@pytest.fixture
def shared_data():
    return {}

@given("I am a standard user on the login page")
def standard_user_on_landing_page(browser_instance, shared_data):
    login_page = LoginPageObjects(browser_instance)
    login_page.navigate_to_login_page()
    shared_data["login_page"] = login_page

@when(parsers.parse("I login to Sauce Demo with {username} and {password}"))
def login_to_sauce_demo(username, password, shared_data):
    login_page = shared_data["login_page"]
    products_page = login_page.login(username, password)
    shared_data["products_page"] = products_page

@then("I should see the Products page")
def see_products_page(shared_data):
    products_page = shared_data["products_page"]
    products_page.verify_page_title()

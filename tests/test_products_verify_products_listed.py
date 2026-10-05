from pytest_bdd import given, when, then, parsers, scenarios
import pytest

from pageobjects.login_page_objects import LoginPageObjects

scenarios("../features/products_verify_products_listed.feature")

@pytest.fixture
def shared_data():
    return {}

@given("a standard user is on the login page")
def standard_user_on_landing_page(browser_instance, shared_data):
    login_page = LoginPageObjects(browser_instance)
    login_page.navigate_to_login_page()
    shared_data["login_page"] = login_page

@when(parsers.parse("the standard user logins to Sauce Demo with {username} and {password}"))
def login_to_sauce_demo(username, password, shared_data):
    login_page = shared_data["login_page"]
    products_page = login_page.login(username, password)
    shared_data["products_page"] = products_page

@when("the standard user should see the Products page")
def see_products_page(shared_data):
    products_page = shared_data["products_page"]
    products_page.verify_page_title()

@then("the standard user should see the following products listed:")
def verify_products_list(shared_data, datatable):
    products_page = shared_data["products_page"]
    products = products_page.get_product_list()
    expected_products = {name: {"image": image, "cost": cost} for name, image, cost in datatable[1:]}
    products_page.compare_product_lists(products, expected_products)

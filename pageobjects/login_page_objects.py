from playwright.sync_api import Page

from pageobjects.products_page_objects import ProductsPageObjects

class LoginPageObjects:

    def __init__(self, page: Page):

        self.page = page
        self.loginlogo = page.locator(".login_logo")
        self.usernamefield = page.locator("#user-name")
        self.passwordfield = page.locator("#password")
        self.loginbtn = page.locator("#login-button")
        self.errormsg = page.locator("[data-test='error']")
        self.loginbox = page.locator(".login-box")

    def navigate_to_login_page(self):
            self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):

        print(f'Entering "{username}" for username')
        self.usernamefield.fill(username)

        print(f'Entering password for "{username}"')
        self.passwordfield.fill(password)

        print(f'Clicking "Login" btn')
        self.loginbtn.click()
        return ProductsPageObjects(self.page)

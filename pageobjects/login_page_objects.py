from playwright.sync_api import Page, expect, Playwright

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

        print(f'\nEntering "{username}" for username')
        self.usernamefield.fill(username)

        print(f'Entering password for "{username}"')
        self.passwordfield.fill(password)

        print(f'Clicking "Login" btn')

        try:
            self.loginbtn.click(timeout=2000)
        except PlaywrightTimeoutError:
            raise AssertionError ("Login took too long, should be less than 2 seconds")

        return ProductsPageObjects(self.page)

    def verify_user_locked_out_message(self):
        expect(self.errormsg).to_contain_text("user has been locked out")
        print("User locked out message displayed successfully")

    def verify_login_box_visible(self):
        expect(self.loginbox).to_be_visible()
        print("User remains on login page after locked out message")

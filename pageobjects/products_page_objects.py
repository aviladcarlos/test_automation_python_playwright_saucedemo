from playwright.sync_api import Page, expect


class ProductsPageObjects:

    def __init__(self, page: Page):
        self.page = page
        self.pagetitle = page.locator(".title")

    def verify_page_title(self):
        print(self.pagetitle)
        expect(self.pagetitle).to_have_text("Products")
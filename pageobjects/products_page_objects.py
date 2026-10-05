from playwright.sync_api import Page, expect


class ProductsPageObjects:

    def __init__(self, page: Page):
        self.page = page
        self.pagetitle = self.page.locator(".title")
        self.productlist = self.page.locator(".inventory_item")
        self.shoppingcartlink = self.page.locator(".shopping_cart_link")

        # Locators chain with productlist
        self.productlist_name_locator = ".inventory_item_name"
        self.productlist_image_locator = "img"
        self.productlist_price_locator = ".inventory_item_price"
        self.productlist_btn_addtocart_locator = "button"


    def verify_page_title(self):
        expect(self.pagetitle).to_have_text("Products")
        print("User logged in successfully")

    def get_product_list(self):
        products = {}

        for product in self.productlist.all():
            products[product.locator(self.productlist_name_locator).inner_text()] = \
                {
                    "image" : product.locator(self.productlist_image_locator).get_attribute("src"),
                    "cost": product.locator(self.productlist_price_locator).inner_text(),
                }

        return products

    @staticmethod
    def compare_product_lists(products, expected_products):
        products = products
        expected_products = expected_products
        products_incorrect_image = []
        products_incorrect_cost = []

        # If there is more products on the site than in expected products dict throws a warning that
        # prints the products on the site that are not included in expected products dict.
        if len(products) > len(expected_products):
            print(f"Warning: The following {len(products) - len(expected_products)}"
                  f" products on the site are not listed in expected products dict:")

            for product in products:
                if product not in expected_products:
                    print(f"Warning:    -{product}")

        # If there is more products in the expected products dict than what is listed on the site throws a warning that
        # prints the products on the expected products dict that are not included on the site.
        elif len(products) < len(expected_products):
            print(f"Warning: The following {len(expected_products) - len(products)}"
                  f" products in expected products dict are not listed on the site:")

            for product in expected_products:
                if product not in products:
                    print(f"Warning:    -{product}")

        for product in products:

            if product in expected_products:
                print(f'Verifying image url and cost of "{product}"')

                # Verify image matches with expected url
                if products[product]["image"] != expected_products[product]["image"]:
                    print(f"    Image Test failed: Image url does not match with expected image url:")
                    print(f"    Result: {products[product]["image"]}")
                    print(f"    Expected Result: {expected_products[product]["image"]}")
                    products_incorrect_image.append(product)

                # Verify displayed cost matches with expected cost
                if products[product]["cost"] != expected_products[product]["cost"]:
                    print(f"    Cost Test failed: Listed cost does not match with expected cost:")
                    print(f"    Result: {products[product]["cost"]}")
                    print(f"    Expected Result: {expected_products[product]["cost"]}")
                    products_incorrect_cost.append(product)

        # If there is incorrect information on a product throws this error:
        assert (len(products_incorrect_image) == 0 and len(products_incorrect_cost) == 0),\
            "Test failed: 1 or more products on site has incorrect information, view log for more information."

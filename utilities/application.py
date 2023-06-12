from playwright.sync_api import Playwright

from pages.pages import (
    MainPage,
    SignInPage,
    RegistrationPage,
    ReptileCategoryPage,
    ProductsPage
)


class App:
    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url

        # Pages
        self.main_page = MainPage(self.page)
        self.sign_in_page = SignInPage(self.page)
        self.registration_page = RegistrationPage(self.page)
        self.reptile_category_page = ReptileCategoryPage(self.page)
        self.products_page = ProductsPage(self.page)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()

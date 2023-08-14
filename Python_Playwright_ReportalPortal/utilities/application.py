import logging

from playwright.sync_api import Playwright, ConsoleMessage, Dialog

from Python_Playwright_ReportalPortal.pages.pages import (
    MainPage,
    SignInPage,
    RegistrationPage,
    ReptileCategoryPage,
    ProductsPage,
    ShoppingCartPage,
    NewOrderFormPage,
    OrderFormPage,
    OrderPage,
    MyAccountPage,
    MyOrdersPage
)


class App:
    def __init__(self, playwright: Playwright, base_url: str, headless=True):

        def console_handler(message: ConsoleMessage):
            if message.type == "error":
                logging.error(f"PAGE: {self.page.url}, CONSOLE_ERROR: {message.text}")

        def dialog_handler(dialog: Dialog):
            logging.warning(f"PAGE: {self.page.url}, DIALOG_TEXT: {dialog.message}")
            dialog.accept()

        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url
        self.page.on("console", console_handler)
        self.page.on("dialog", dialog_handler)

        # Pages
        self.main_page = MainPage(self.page)
        self.sign_in_page = SignInPage(self.page)
        self.registration_page = RegistrationPage(self.page)
        self.reptile_category_page = ReptileCategoryPage(self.page)
        self.products_page = ProductsPage(self.page)
        self.shopping_cart_page = ShoppingCartPage(self.page)
        self.new_order_form_page = NewOrderFormPage(self.page)
        self.order_form_page = OrderFormPage(self.page)
        self.order_page = OrderPage(self.page)
        self.my_account_page = MyAccountPage(self.page)
        self.my_order_page = MyOrdersPage(self.page)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()

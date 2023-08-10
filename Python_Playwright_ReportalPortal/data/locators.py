class MainPageLocators:
    MAIN_PAGE_URL = "https://petstore.octoperf.com/actions/Catalog.action"

    # SideBar Menu
    SIDEBAR_MENU = "//div[@id='Sidebar']"
    REPTILES_CATEGORY_IN_SIDEBAR_MENU = "//div[@id='Sidebar']//a[contains(@href, 'REPTILES')]"

    # Header Menu
    SIGN_IN_BUTTON = "//div[@id='MenuContent']/a[text()='Sign In']"
    SHOPPING_CART_BUTTON = "//div[@id='MenuContent']/a[1]"
    MY_ACCOUNT_BUTTON = "//div[@id='MenuContent']/a[text()='My Account']"

    # Main Page Content
    WELCOME_MESSAGE = "//div[@id='WelcomeContent']"


class SignInPageLocators:
    REGISTER_BUTTON = "//a[contains(text(),'Register Now!')]"
    USERNAME_INPUT = "//input[@name='username']"
    PASSWORD_INPUT = "//input[@name='password']"
    LOGIN_BUTTON = "//input[@name='signon']"
    SIGN_ON_FAILED_MESSAGE = "//ul[@class='messages']"


class RegistrationPageLocators:

    # User Information

    USER_ID = "//input[@name='username']"
    NEW_PASSWORD = "//input[@name='password']"
    REPEAT_PASSWORD = "//input[@name='repeatedPassword']"

    # Account Information

    FIRST_NAME = "//input[@name='account.firstName']"
    LAST_NAME = "//input[@name='account.lastName']"
    EMAIL = "//input[@name='account.email']"
    PHONE = "//input[@name='account.phone']"
    ADDRESS_1 = "//input[@name='account.address1']"
    ADDRESS_2 = "//input[@name='account.address2']"
    CITY = "//input[@name='account.city']"
    STATE = "//input[@name='account.state']"
    ZIP = "//input[@name='account.zip']"
    COUNTRY = "//input[@name='account.country']"

    # Profile Information

    LANGUAGE_PREFERENCE = "//select[@name='account.languagePreference']"
    FAVOURITE_CATEGORY = "//select[@name='account.favouriteCategoryId']"
    MY_LIST = "//input[@name='account.listOption']"
    MY_BANNER = "//input[@name='account.bannerOption']"

    SAVE_ACCOUNT_INFORMATION_BUTTON = "//input[@name='newAccount']"


class ReptileCategoryPageLocators:
    @staticmethod
    def product_item_by_name(product_name: str) -> str:
        return str(f"//td[..//td[text()='{product_name}']]/a")


class ProductsPageLocators:
    FIRST_PRODUCT_ADD_TO_CART_BUTTON = "//a[@class='Button'][1]"


class ShoppingCartPageLocators:
    REMOVE_BUTTON = "//a[@class='Button' and text()='Remove']"
    UPDATE_CART_BUTTON = "//input[@name='updateCartQuantities']"
    PROCEED_TO_CHECKOUT_BUTTON = "//div[@id='Cart']/a[@class='Button']"
    LIST_PRICE = "//td[contains(text(), '$')][..//td/input[@size]][1]"
    TOTAL_COAST = "//td[contains(text(), '$')][..//td/input[@size]][2]"
    INPUT_QUANTITY = "//td/input[@size]"


class NewOrderFormPageLocators:
    CONTINUE_BUTTON = "//input[@name='newOrder']"


class OrderFormPageLocators:
    CONFIRM_BUTTON = "//a[@class='Button' and text()='Confirm']"


class OrderPageLocators:
    ORDER_HEADER = "//th[starts-with(text(), 'Order #')]"     # Order #114274 2023/06/14 09:17:35


class MyAccountPageLocators:
    MY_ORDERS_BUTTON = "//div[@id='Catalog']/a[text()='My Orders']"


class MyOrdersPageLocators:
    @staticmethod
    def order_id_by_number(order_number: str) -> str:
        return str(f"//div[@id='Content']//td/a[text()='{order_number}']")

    ORDER_ID = "//div[@id='Content']//td/a"

class MainPageLocators:
    MAIN_PAGE_URL = "https://petstore.octoperf.com/actions/Catalog.action"

    # SideBar Menu
    SIDEBAR_MENU = "//div[@id='Sidebar']"
    REPTILES_CATEGORY_IN_SIDEBAR_MENU = "//div[@id='Sidebar']//a[contains(@href, 'REPTILES')]"

    SIGN_IN_BUTTON = "//div[@id='MenuContent']/a[text()='Sign In']"
    SHOPPING_CART_BUTTON = "//div[@id='MenuContent']/a[1]"
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
    def product_item_by_name(product_name: str):
        return str(f"//td[..//td[text()='{product_name}']]/a")


class ProductsPageLocators:
    FIRST_PRODUCT_ADD_TO_CART_BUTTON = "//a[@class='Button'][1]"

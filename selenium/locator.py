from selenium.webdriver.common.by import By


class MainPageLocators():
    PRODUCTS_BUTTON = (By.XPATH, "//a[@class='dropdown-item']")
    CART_SIZE = (By.CLASS_NAME, "cart-products-count")
    CART_BUTTON = (By.CLASS_NAME, "shopping-cart")
    SIGN_IN_BUTTON = (By.CLASS_NAME, "user-info")

class ProductsPageLocators():
    CATEGORY_BUTTONS = (By.CLASS_NAME, "subcategory-name")
    HOME_PAGE_BUTTON = (By.CLASS_NAME, "logo")

class ProductsCategoryPageLocators():
    PRODUCTS_BUTTONS = (By.CLASS_NAME, "thumbnail.product-thumbnail")

class ProductPageLocators():
    NUMBER_OF_ITEM = (By.NAME , "qty")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "add-to-cart")
    CART_POP_UP = (By.ID, "myModalLabel")
    CLOSE_CART_POP_UP_BUTTON = (By.XPATH, "//button[text()='Kontynuuj zakupy']")
    HOME_PAGE_BUTTON = (By.CLASS_NAME, "logo")
    HOW_MANY = (By.XPATH, "//span[@data-stock]")


class CartPageLocators():
    DELETE_BUTTON = (By.CLASS_NAME, "remove-from-cart")
    NUMBER_OF_UNIQUE_ITEMS = (By.CLASS_NAME, "cart-item")
    CHECKOUT_BUTTON = (By.CLASS_NAME, "checkout")
    SIGN_IN_BUTTON = (By.CLASS_NAME, "user-info")

class CheckoutPageLocators():
    GENDER_MALE_RADIO_BUTTON = (By.ID, "field-id_gender-1")
    NAME_FIELD = (By.ID, "field-firstname")
    SURNAME_FIELD = (By.ID, "field-lastname")
    EMAIL_FIELD = (By.ID, "field-email")
    PRIVACY_CHECK_BOX = (By.NAME, "customer_privacy")
    TERMS_OF_USE_CHECK_BOX = (By.NAME, "psgdpr")
    REGISTER_NEW_CUSTOMER_BUTTON = (By.XPATH, "//button[@data-link-action='register-new-customer']")
    ADRESS_FIELD = (By.ID, "field-address1")
    POST_CODE_FIELD = (By.ID, "field-postcode")
    CITY_FIELD = (By.ID, "field-city")
    CONFIRM_ADDRESS_BUTTON = (By.NAME, "confirm-addresses")
    DELIVERY_TYPE_RADIO_BUTTON = (By.ID, "delivery_option_2")
    CONFIRM_DELIVERY_BUTTON = (By.NAME, "confirmDeliveryOption")
    TERMS_OF_PAYMENT_CHECK_BOX = (By.ID, "conditions_to_approve[terms-and-conditions]")
    SUBMIT_ORDER_BUTTON = (By.CLASS_NAME, "btn.btn-primary.center-block")
    PAYMENT_TYPE_RADIO_BUTTON = (By.ID, "payment-option-2")

class LoginPageLocators():
    REGISTER_NEW_USER_LINK = (By.XPATH, "//a[@data-link-action='display-register-form']")

class RegisterPageLocators():
    GENDER_MALE_RADIO_BUTTON = (By.ID, "field-id_gender-1")
    NAME_FIELD = (By.ID, "field-firstname")
    SURNAME_FIELD = (By.ID, "field-lastname")
    EMAIL_FIELD = (By.ID, "field-email")
    PASSWORD_FIELD = (By.ID, "field-password")
    BIRTH_DATE_FIELD = (By.ID, "field-birthday")
    PRIVACY_CHECK_BOX = (By.NAME, "customer_privacy")
    TERMS_OF_USE_CHECK_BOX = (By.NAME, "psgdpr")
    REGISTER_NEW_CUSTOMER_BUTTON = (By.XPATH, "//button[@data-link-action='save-customer']")

class AfterPurchasePageLocators():
    HOME_PAGE_BUTTON = (By.CLASS_NAME, "logo")
    PROFIL_LINK = (By.CLASS_NAME, "account")

class AccountPageLocators():
    HISTORY_BUTTON = (By.ID, "history-link")

class HistoryPageLocators():
    ORDER_DETAILS_LINKS = (By.XPATH, "//a[@data-link-action='view-order-details']")
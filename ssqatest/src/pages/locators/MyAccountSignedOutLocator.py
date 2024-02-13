from selenium.webdriver.common.by import By

class MyAccountSignedOutLocator:

    LOGIN_USER_NAME = (By.ID, 'username')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.NAME, 'login')

    ERRORS_UL = (By.CSS_SELECTOR, 'ul.woocommerce-error')

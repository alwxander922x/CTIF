from selenium.webdriver.common.by import By

class MyAccountSignedOutLocator:

    LOGIN_USER_NAME = (By.ID, 'username')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.NAME, 'login')
    ERRORS_UL = (By.CSS_SELECTOR, 'ul.woocommerce-error')

    REGISTER_EMAIL = (By.ID, 'reg_email')
    REGISTER_PASSWORD = (By.ID, 'reg_password')
    REGISTER_BTN = (By.CSS_SELECTOR, '#customer_login > div.u-column2.col-2 > form > p:nth-child(4) > button')
    # REGISTER_BTN = (By.CSS_SELECTOR, 'button[value="Register"]')
    # REGISTER_SUCCESS = (By.XPATH, "//div[@class='woocommerce-notices-wrapper']")
    REGISTER_SUCCESS = (By.CSS_SELECTOR, "#post-9 > div > div > div > p:nth-child(2)")
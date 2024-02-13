import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions

@pytest.fixture(scope="class")
def init_driver(request):

    pass
    supported_browsers = ['chrome', 'firefox']

    browser = os.environ.get('BROWSER')
    if not browser:
        raise Exception("The env variable BROWSER is not set")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"{browser} is not supported")


    if browser in 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser in 'firefox':
        driver = webdriver.Firefox()
    # elif browser in('headleeschrome'):
    #     chrome_options = ChOptions()
    #     chrome_options.add_argument('--disable-gpu')
    #     chrome_options.add_argument('--no--sandbox')
    #     chrome_options.add_argument('--headless')
    #     driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield
    # driver.quit()
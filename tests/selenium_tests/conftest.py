import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from .config import *


@pytest.fixture()
def wait(browser):
    wait = WebDriverWait(browser, WAIT)
    return wait


@pytest.fixture(scope="session")
def browser():
    service = Service(executable_path=ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(WAIT)

    yield browser
    browser.quit()

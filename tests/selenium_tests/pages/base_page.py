from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, wait, base_url):
        self.wait = wait
        self.browser = browser
        self.base_url = base_url

    def open(self):
        return self.browser.get(self.base_url)

    def is_element_present(self, how, what):
        try:
            self.wait.until(EC.presence_of_all_elements_located((how, what)))
        except TimeoutException:
            return False
        return True

    def double_click(self, what):
        action = ActionChains(self.browser)
        action.double_click(what).perform()

    def wait_for_url(self):
        url = self.browser.current_url
        self.wait.until(lambda driver: driver.current_url != url)

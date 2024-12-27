from .base_page import BasePage
from .locators import TrajectoriesTestPageLocators


class TrajectoriesAuthPage(BasePage):
    def accept_cookies(self):
        if self.is_element_present(*TrajectoriesTestPageLocators.COOKIES_BUTTON):
            self.browser.find_element(*TrajectoriesTestPageLocators.COOKIES_BUTTON).click()

    def go_to_auth_by_ETU_ID(self):
        if self.is_element_present(*TrajectoriesTestPageLocators.AUTH_BY_ETU_ID_BUTTON):
            self.browser.find_element(*TrajectoriesTestPageLocators.AUTH_BY_ETU_ID_BUTTON).click()

        if self.is_element_present(*TrajectoriesTestPageLocators.LK_AUTH_BY_ETU_ID_BUTTON):
            self.browser.find_element(*TrajectoriesTestPageLocators.LK_AUTH_BY_ETU_ID_BUTTON).click()

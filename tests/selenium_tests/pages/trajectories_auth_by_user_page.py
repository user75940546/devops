from tests.selenium_tests.pages.base_page import BasePage
from tests.selenium_tests.pages.locators import AuthByUserPageLocators


class TrajectoriesAuthByUserPage(BasePage):
    def apply_role_filter(self, role_name):
        if self.is_element_present(*AuthByUserPageLocators.ROLE_FILTER_BUTTON):
            self.browser.find_element(*AuthByUserPageLocators.ROLE_FILTER_BUTTON).click()
            if self.is_element_present(*AuthByUserPageLocators.ROLE_FILTER(role_name)):
                self.browser.find_element(*AuthByUserPageLocators.ROLE_FILTER(role_name)).click()

    def find_user(self, id):
        if self.is_element_present(*AuthByUserPageLocators.USER(id)):
            return self.browser.find_element(*AuthByUserPageLocators.USER(id))

    def authorize_by_user(self, id):
        start, end = (self.browser.find_element(*AuthByUserPageLocators.START),
                      self.browser.find_element(*AuthByUserPageLocators.END),)

        condition = True

        while condition:
            start_value = int(start.text.replace(",", ""))
            end_value = int(end.text.replace(",", ""))

            condition = not (start_value <= id <= end_value)

            if condition:
                self.browser.find_element(*AuthByUserPageLocators.NEXT_PAGE).click()
                start, end = (self.browser.find_element(*AuthByUserPageLocators.START),
                              self.browser.find_element(*AuthByUserPageLocators.END),)

        user = self.find_user(id)
        self.double_click(user)

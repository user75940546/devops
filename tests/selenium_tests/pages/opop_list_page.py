import re

from tests.selenium_tests.pages.base_page import BasePage
from tests.selenium_tests.pages.locators import OpopListPageLocators


class OpopListPage(BasePage):
    def add_document(self, name, plan_name):
        self.browser.find_element(*OpopListPageLocators.ADD_DOCUMENT_BUTTON).click()

        name_element, plan_name_element = self.browser.find_elements(*OpopListPageLocators.ADD_DOCUMENT_INPUTS)

        name_element.click()
        name_element.find_element(*OpopListPageLocators.ADD_DOCUMENT_OPTION(name)).click()

        plan_name_element.click()
        plan_name_element.find_element(*OpopListPageLocators.ADD_DOCUMENT_OPTION(plan_name)).click()

        self.browser.find_element(*OpopListPageLocators.ADD_DOCUMENT_SUBMIT_BUTTON).click()

        self.wait_for_url()

        return re.search(r"/opop/(\d+)", self.browser.current_url).group(1)

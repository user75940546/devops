from tests.selenium_tests.pages.base_page import BasePage
from tests.selenium_tests.pages.locators import EtuAuthPageLocators


class EtuAuthPage(BasePage):
    def authorize(self, login, password):
        assert self.is_element_present(*EtuAuthPageLocators.LOGIN_INPUT), "На форме авторизации нет поля ввода email"
        self.browser.find_element(*EtuAuthPageLocators.LOGIN_INPUT).send_keys(login)
        assert self.is_element_present(
            *EtuAuthPageLocators.PASSWORD_INPUT), "На форме авторизации нет поля ввода пароля"
        self.browser.find_element(*EtuAuthPageLocators.PASSWORD_INPUT).send_keys(password)
        assert self.is_element_present(
            *EtuAuthPageLocators.REMEMBER_ME_BUTTON), "На форме авторизации отсутствует кнопка запомнить"
        self.browser.find_element(*EtuAuthPageLocators.REMEMBER_ME_BUTTON).click()
        self.browser.find_element(*EtuAuthPageLocators.SUBMIT_BUTTON).click()

    def accept_authorize_oauth(self):
        assert self.is_element_present(*EtuAuthPageLocators.OAUTH_SUBMIT_FORM), "Не найдена форма аутентификации oauth"
        self.browser.find_element(*EtuAuthPageLocators.OAUTH_SUBMIT_BUTTON).click()

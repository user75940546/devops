from selenium.webdriver.common.by import By


class TrajectoriesTestPageLocators:
    AUTH_BY_ETU_ID_BUTTON = (By.XPATH, '//button[contains(text(), "Войти через ETU ID")]',)
    LK_AUTH_BY_ETU_ID_BUTTON = (By.XPATH, './/button[@data-eid="login"]')
    COOKIES_BUTTON = (By.XPATH, './/button[@data-cy="cookies-ok-button"]')


class EtuAuthPageLocators:
    LOGIN_INPUT = (By.XPATH, './/input[@type="email"]')
    PASSWORD_INPUT = (By.XPATH, './/input[@type="password"]')
    REMEMBER_ME_BUTTON = (By.ID, "remember")
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    OAUTH_SUBMIT_FORM = (By.XPATH, '//form[@action="https://lk.etu.ru/oauth/authorize"]',)
    OAUTH_SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')


class AuthByUserPageLocators:
    ROLE_FILTER_BUTTON = (By.XPATH, '//div[@col-id="roles"]//span[@ref="eMenu"]')
    ROLE_FILTER = lambda role: (By.XPATH, f'//div[contains(@class, "ag-filter")]//p[contains(text(),"{role}")]',)
    USER = lambda id: (By.XPATH, f'//div[@ref="eCenterContainer"]//div[@col-id="id"]//span[contains(text(),"{id}")]',)
    NEXT_PAGE = (By.XPATH, '//button[contains(text(),"Next")]')
    START = (By.XPATH, '//span[@ref="lbFirstRowOnPage"]')
    END = (By.XPATH, '//span[@ref="lbLastRowOnPage"]')


class OpopListPageLocators:
    ADD_DOCUMENT_BUTTON = (By.XPATH, '//button[contains(text(), "Добавить")]')
    ADD_DOCUMENT_INPUTS = (By.CSS_SELECTOR, ".multiselect")
    ADD_DOCUMENT_OPTION = lambda option: (By.XPATH, f'//span[text()="{option}"]')
    ADD_DOCUMENT_SUBMIT_BUTTON = (
        By.XPATH, '//div[@id="creationModalId___BV_modal_content_"]//button[contains(text(), "Добавить")]',)


class DocumentOpopPageLocators:
    TAB_LIST_ITEM = lambda tab_id: (By.XPATH, f'//ul[@role="tablist"]//a[@aria-posinset="{tab_id}"]',)
    SAVE_DOCUMENT_BUTTON = (By.CSS_SELECTOR, 'span[title^="Сохранить документ"]')
    JSON_PREVIEW_BUTTON = (By.XPATH, '//ul[contains(@class, "nav")]//a[contains(text(),"Превью JSON (dev)")]',)
    JSON_COPY_BUTTON = (By.XPATH, '//div[contains(@class, "jv-container")]//span[contains(text(),"copy")]',)

    BASE_TABLE_ROW = (By.XPATH, '//div[@role="row"]')
    BASE_TABLE_ROW_CELL = lambda id_array: (By.XPATH,
                                            f"""//div[contains(@class, "ag-cell") and ({" or ".join([f"@col-id='{id}'" for id in id_array])})]""",)
    BASE_TABLE_ROW_CELL_INPUT = (By.XPATH, '//input[@type="text"]')
    BASE_TABLE_ROW_CLEAR_BUTTON = (
        By.CSS_SELECTOR, '.ag-pinned-right-cols-container div[role^="row"] button:first-of-type',)

    DATE_PICKER_WIDGET = (By.CSS_SELECTOR, ".mx-datepicker")
    DATE_PICKER_WIDGET_INPUT = (By.XPATH, '//input[@name="date"]')

    TAB_7_TABLE_ROWS_CONTAINER = (By.XPATH, '//div[@ref="eCenterColsClipper"]')
    TAB_7_TABLE_ACTION = (By.XPATH, '//div[@role="group"]//button[@type="button"]')

    TAB_MODULES_CONTENT = (By.CSS_SELECTOR, ".moduleSettings")
    TAB_MODULES_EXPAND_ALL_BUTTON = (By.XPATH, '//button[@title="Развернуть всю таблицу"]',)
    TAB_MODULES_TABLE = (By.CSS_SELECTOR, ".modulesTree tbody")
    TAB_MODULES_TABLE_ROW = (By.CSS_SELECTOR, "tr")
    TAB_MODULES_TABLE_CELL = (By.CSS_SELECTOR, "td")
    TAB_MODULES_TABLE_ROW_NAME = (By.CSS_SELECTOR, "span.vxe-cell--label")
    TAB_MODULES_COPY = (By.XPATH, './/button[@title="Копировать РП"]')
    TAB_MODULES_COPY_MODAL = (By.CSS_SELECTOR, "#rpdCopyModal___BV_modal_content_")
    TAB_MODULES_COPY_MODAL_SUBMIT_BTN = (By.XPATH, '//button[contains(text(), "Копировать")]',)

    MULTISELECT = (By.CSS_SELECTOR, ".field-multiselect .multiselect:not(.multiselect--disabled)",)
    MULTISELECT_CONTENT = (By.CSS_SELECTOR, ".multiselect__content")
    MULTISELECT_CONTENT_OPTION = (By.XPATH,
                                  './/span[contains(@class, "multiselect__option") and not(contains(@class, "multiselect__option--disabled"))]',)

    TOAST_HEADER_BUTTON = (By.CSS_SELECTOR, ".toast-header button")

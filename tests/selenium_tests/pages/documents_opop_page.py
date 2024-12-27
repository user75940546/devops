import time
import tkinter as tk
from functools import partial

from tests.selenium_tests.json_utils import *
from tests.selenium_tests.pages.base_page import BasePage
from tests.selenium_tests.pages.locators import DocumentOpopPageLocators


class DocumentsOpopPage(BasePage):
    def __init__(self, browser, wait, base_url):
        super().__init__(browser, wait, base_url)
        self.fill_document_cfg = {
            7: partial(
                self.fill_base_table,
                DocumentOpopPageLocators.TAB_7_TABLE_ROWS_CONTAINER,
                DocumentOpopPageLocators.TAB_7_TABLE_ACTION,
                read_test_data("listRegistrationChanges.json"),
                {
                    "dateOfChange": "date-picker",
                    "changes": "text",
                    "dateMeeting": "date-picker",
                    "numberProtocol": "text",
                    "headOPOP": "text",
                    "headOMOLA": "text",
                },
            ),
            13: partial(
                self.fill_modules,
                read_test_data("modules.json"),
            ),
        }

    def fill_document(self):
        for tab_id, fn in self.fill_document_cfg.items():
            self.move_to_tab(tab_id)
            fn()
            self.close_toast()
            self.save_document()

    def move_to_tab(self, tab):
        tab_id = tab if tab == 1 else tab + 1
        self.browser.find_element(*DocumentOpopPageLocators.TAB_LIST_ITEM(tab_id)).click()

    def save_document(self):
       self.browser.find_element(*DocumentOpopPageLocators.SAVE_DOCUMENT_BUTTON).click()

    def close_toast(self):
        if self.is_element_present(*DocumentOpopPageLocators.TOAST_HEADER_BUTTON):
            self.browser.find_element(*DocumentOpopPageLocators.TOAST_HEADER_BUTTON).click()

    def get_json(self):
        self.move_to_tab(1)
        self.browser.find_element(*DocumentOpopPageLocators.JSON_PREVIEW_BUTTON).click()
        self.browser.find_element(*DocumentOpopPageLocators.JSON_COPY_BUTTON).click()

        root = tk.Tk()
        root.withdraw()

        try:
            clipboard_text = root.clipboard_get()
            return json.loads(clipboard_text)
        except json.JSONDecodeError as e:
            raise ValueError(e)
        except tk.TclError as e:
            raise ValueError(e)
        finally:
            root.destroy()

    def fill_modules(self, modules):
        if self.is_element_present(*DocumentOpopPageLocators.TAB_MODULES_CONTENT):
            self.browser.find_element(*DocumentOpopPageLocators.TAB_MODULES_EXPAND_ALL_BUTTON).click()

        modules_table = self.browser.find_element(*DocumentOpopPageLocators.TAB_MODULES_TABLE)
        modules_table_rows = modules_table.find_elements(*DocumentOpopPageLocators.TAB_MODULES_TABLE_ROW)

        for row in modules_table_rows:
            cells = row.find_elements(*DocumentOpopPageLocators.TAB_MODULES_TABLE_CELL)
            cell_text = cells[3].find_element(*DocumentOpopPageLocators.TAB_MODULES_TABLE_ROW_NAME)
            if cell_text.text.strip() in modules:
                if not row.find_elements(*DocumentOpopPageLocators.TAB_MODULES_COPY):
                    continue

                row.find_element(*DocumentOpopPageLocators.TAB_MODULES_COPY).click()

                if self.is_element_present(*DocumentOpopPageLocators.TAB_MODULES_COPY_MODAL):
                    modal = self.browser.find_element(*DocumentOpopPageLocators.TAB_MODULES_COPY_MODAL)
                    multiselects = modal.find_elements(*DocumentOpopPageLocators.MULTISELECT)

                    for i, multiselect in enumerate(multiselects):
                        multiselect.click()
                        time.sleep(1)
                        options = multiselect.find_elements(*DocumentOpopPageLocators.MULTISELECT_CONTENT_OPTION)
                        if len(options) > 1:
                            options[1].click()

                    modal.find_element(*DocumentOpopPageLocators.TAB_MODULES_COPY_MODAL_SUBMIT_BTN).click()

    def fill_base_table(self, table_rows_container_locator, table_action_locator, test_data, fields):
        def run_cell_handler(handler, cell, value):
            self.double_click(cell)
            handler(cell, value)
            self.browser.execute_script("document.activeElement.blur();")

        def handle_cell_date_picker(_, value):
            date_picker = self.browser.find_element(*DocumentOpopPageLocators.DATE_PICKER_WIDGET)
            date_picker_input = date_picker.find_element(*DocumentOpopPageLocators.DATE_PICKER_WIDGET_INPUT)
            date_picker_input.send_keys(value)

        def handle_cell_text_field(cell, value):
            cell.find_element(*DocumentOpopPageLocators.BASE_TABLE_ROW_CELL_INPUT).send_keys(value)

        handlers = {
            "date-picker": lambda cell, value: run_cell_handler(handle_cell_date_picker, cell, value),
            "text": lambda cell, value: run_cell_handler(handle_cell_text_field, cell, value),
        }

        self.clear_base_table()

        table_rows_container = self.browser.find_element(*table_rows_container_locator)
        action_element = self.browser.find_element(*table_action_locator)

        target_row_count = len(test_data)

        for _ in range(target_row_count):
            action_element.click()

        table_row_elements = table_rows_container.find_elements(*DocumentOpopPageLocators.BASE_TABLE_ROW)

        for i, test_obj in enumerate(test_data):
            row = table_row_elements[i]

            cells = row.find_elements(*DocumentOpopPageLocators.BASE_TABLE_ROW_CELL(fields))

            for _, (field, cell) in enumerate(zip(fields.items(), cells)):
                field_name, field_handler_type = field
                value = test_obj.get(field_name) or ""
                self.double_click(cell)

                handler = handlers.get(field_handler_type)

                if handler:
                    handler(cell, value)

    def clear_base_table(self):
        table_cleat_btns = self.browser.find_elements(*DocumentOpopPageLocators.BASE_TABLE_ROW_CLEAR_BUTTON)
        for btn in table_cleat_btns:
            btn.click()

    def filter_auto_data(self, data):
        return [item for item in data if item.get("isAuto") != True]

    def is_document_saved(self):
        listRegistrationChanges_json = from_json_get_by_path(self.get_json(), "changeHistory.listRegistrationChanges")
        json_compare(
            self.filter_auto_data(listRegistrationChanges_json),
            read_test_data("listRegistrationChanges.json"),
        )
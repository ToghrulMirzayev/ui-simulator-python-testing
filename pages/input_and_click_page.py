"""
InputAndClickPage class represents corresponding page
"""

from __future__ import annotations
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from base.base_object import BaseObject
from support.assertions import Assertions


class InputAndClickPage(BaseObject, Assertions):
    INPUT_FIELD: tuple = (By.ID, "inputText")
    ADD_BTN: tuple = (By.ID, "addBtn")
    DELETE_BTN: tuple = (By.ID, "deleteBtn")
    ITEM_LIST: tuple = lambda self, index: (By.CSS_SELECTOR, f"#items div:nth-child({index})")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def add_new_item(self, value: str, item_index: str | int) -> None:
        self._enter_item(value)
        self._add_item()
        self._is_item_added(value, item_index)

    def _enter_item(self, value: str) -> None:
        self.send_keys(self.INPUT_FIELD, value)

    def _add_item(self) -> None:
        self.click(self.ADD_BTN)

    def _is_item_added(self, value: str, item_index: str) -> None:
        self.is_equal(actual=self.get_text(self.ITEM_LIST(item_index)),
                      expected=value)

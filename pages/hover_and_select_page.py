"""
HoverAndSelectPage class represents corresponding page
"""

from __future__ import annotations
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from base.base_object import BaseObject
from support.assertions import Assertions


class HoverAndSelectPage(BaseObject, Assertions):
    SELECT_NAVIGATION: tuple = (By.CLASS_NAME, "select-text")
    SELECT_DROPDOWN: tuple = lambda self, index: (By.CSS_SELECTOR, f".dropdown-content li:nth-child({index})")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def navigate(self, page_index: str | int, page: str) -> None:
        self._open_dropdown()
        self._select_from_dropdown(page_index)
        self._is_navigated_page_correct(page)

    def _open_dropdown(self) -> None:
        self.hover(self.SELECT_NAVIGATION)

    def _select_from_dropdown(self, page_index: str | int) -> None:
        self.click(self.SELECT_DROPDOWN(page_index))

    def _is_navigated_page_correct(self, page: str) -> None:
        self.is_equal(actual=self.get_current_url(),
                      expected=page)

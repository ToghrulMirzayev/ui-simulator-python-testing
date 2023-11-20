"""
CheckAndValidatePage class represents corresponding page
"""
from __future__ import annotations

from base.base_object import BaseObject
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions


class CheckAndValidatePage(BaseObject, Assertions):

    VALUE_FIELD: tuple = (By.ID, "dataInput")
    VALIDATION_SQUARE: tuple = (By.ID, "validationSquare")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def perform_validation(self, value: str | int, expected_text: str) -> None:
        self._enter_value(value)
        self._is_valid(expected_text)

    def _enter_value(self, value: str | int) -> None:
        self.send_keys(self.VALUE_FIELD, value)

    def _is_valid(self, expected_text: str) -> None:
        self.is_equal(
            actual=self.get_text(self.VALIDATION_SQUARE),
            expected=expected_text
        )

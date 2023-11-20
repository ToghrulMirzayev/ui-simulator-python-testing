"""
IndexPage class represents the start page
"""

from base.base_object import BaseObject
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions
from env_setup import URLSetup


class IndexPage(BaseObject, Assertions):

    USERNAME_FIELD: tuple = (By.ID, "username")
    PASSWORD_FIELD: tuple = (By.ID, "password")
    LOGIN_BTN: tuple = (By.CLASS_NAME, "login-button")
    ERROR_MSG: tuple = (By.CLASS_NAME, "error-message")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def perform_login(self, username: str, password: str) -> None:
        self._enter_username(username)
        self._enter_password(password)
        self._click_to_login_btn()

    def _enter_username(self, username: str) -> None:
        self.send_keys(self.USERNAME_FIELD, username)

    def _enter_password(self, password: str) -> None:
        self.send_keys(self.PASSWORD_FIELD, password)

    def _click_to_login_btn(self) -> None:
        self.click(self.LOGIN_BTN)

    def is_logged(self) -> None:
        self.is_equal(actual=self.get_current_url(),
                      expected=URLSetup.HOVER_AND_SELECT_PAGE_URL)

    def is_error_msg_correct(self, expected_msg: str) -> None:
        self.is_equal(actual=self.get_text(self.ERROR_MSG),
                      expected=expected_msg)

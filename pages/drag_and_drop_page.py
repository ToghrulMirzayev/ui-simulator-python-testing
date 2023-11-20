"""
DragAndDropPage class represents corresponding page
"""

from base.base_object import BaseObject
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions


class DragAndDropPage(BaseObject, Assertions):

    CARD_ELEMENT: tuple = lambda self, index: (By.CSS_SELECTOR, f"#item-{index}")
    DONE_WORD_ELEMENT: tuple = (By.CLASS_NAME, "done")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def replace_cards(self) -> None:
        elements_to_drag = [("3", "1"), ("2", "1"), ("7", "1"), ("4", "1"), ("6", "5")]

        for source, target in elements_to_drag:
            self.drag_and_drop(self.CARD_ELEMENT(source), self.CARD_ELEMENT(target))

    def is_done_word_appeared(self) -> None:
        self.is_equal(
            actual=self.get_text(self.DONE_WORD_ELEMENT),
            expected="DONE"
        )

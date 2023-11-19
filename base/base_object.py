"""
BaseObject class implements base methods that will be reusable across whole codebase
"""
from selenium.common import TimeoutException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from support.logger import CustomLogger
import logging as log


class BaseObject:

    LOG = CustomLogger(log_level=log.INFO)

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def _is_visible(self, locator: tuple) -> WebElement:
        """
        Protected method that will return visible element
        :param locator: locator to find visible element
        :return: visible element
        """
        try:
            element = self.wait.until(ec.visibility_of_element_located(locator))
            self.LOG.log(f"{locator} is visible")
            return element
        except TimeoutException:
            self.LOG.log(f"{locator} is not visible", level=log.ERROR)
            raise TimeoutException(f"Element {locator} is not visible within the specified timeout")

    def _is_clickable(self, locator: tuple) -> WebElement:
        """
        Protected method that will return clickable element
        :param locator: locator to find clickable element
        :return: clickable element
        """
        try:
            element = self.wait.until(ec.element_to_be_clickable(locator))
            self.LOG.log(f"{locator} is clickable")
            return element
        except TimeoutException:
            self.LOG.log(f"{locator} is not clickable", level=log.ERROR)
            raise TimeoutException(f"Element {locator} is not clickable within the specified timeout")

    def send_keys(self, locator: tuple, value: str) -> None:
        """
        Method that will type text to input field
        :param locator: locator to find input field
        :param value: text that will be typed to the input field
        :return: None
        """
        try:
            self._is_visible(locator).send_keys(value)
            self.LOG.log(f"Typed '{value}' into {locator}")
        except (TimeoutException, ElementNotInteractableException) as e:
            self.LOG.log(f"Failed to type '{value}' into {locator}. {str(e)}", level=log.ERROR)
            raise Exception(f"Failed to type '{value}' into {locator}. {str(e)}")

    def click(self, locator: tuple) -> None:
        """
        Method that will click on clickable element
        :param locator: locator to find element for click
        :return: None
        """
        try:
            self._is_clickable(locator).click()
            self.LOG.log(f"{locator} clicked")
        except (TimeoutException, ElementNotInteractableException) as e:
            self.LOG.log(f"{locator} is not clicked. {str(e)}", level=log.ERROR)
            raise Exception(f"{locator} is not clicked. {str(e)}")

    def get_text(self, locator: tuple) -> str:
        """
        Method that will get text from element
        :param locator: locator to reach out element that will contain required text
        :return: Text
        """
        try:
            text = self._is_visible(locator).text
            self.LOG.log(f"{text} has been taken from {locator}")
            return text
        except (TimeoutException, ElementNotInteractableException) as e:
            self.LOG.log(f"Impossible to get text from {locator}. {str(e)}", level=log.ERROR)
            raise Exception(f"Impossible to get text from {locator}. {str(e)}")

    def get_current_url(self) -> str:
        """
        Get current URL
        :return: URL as str
        """
        try:
            url = self.driver.current_url
            self.LOG.log(f"Current URL is {url}")
            return url
        except (TimeoutException, ElementNotInteractableException) as e:
            self.LOG.log(f"Impossible to get current URL. {str(e)}", level=log.ERROR)
            raise Exception(f"Impossible to get current URL. {str(e)}")

    def hover(self, locator: tuple) -> None:
        """
        Method that will hover over element
        :param locator: element that should be hovered over
        :return: None
        """
        try:
            ActionChains(self.driver).move_to_element(self._is_visible(locator)).perform()
            self.LOG.log(f"Hovered over {locator}")
        except (TimeoutException, ElementNotInteractableException) as e:
            self.LOG.log(f"Impossible to hover over {locator}. {str(e)}", level=log.ERROR)
            raise Exception(f"Impossible to hover over {locator}. {str(e)}")

    def drag_and_drop(self, source: tuple, target: tuple) -> None:
        """
        Method that will drag element from source and drop it to source
        :param source: source element to drag
        :param target: target element to drop
        :return: None
        """
        try:
            source_element = self._is_visible(source)
            target_element = self._is_visible(target)
            ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()
            self.LOG.log(f"{source} dragged and dropped to {target}")
        except (TimeoutException, ElementNotInteractableException) as e:
            self.LOG.log(f"Impossible to drag {source} and drop to {target}. {str(e)}", level=log.ERROR)
            raise Exception(f"Impossible to drag {source} and drop to {target}. {str(e)}")

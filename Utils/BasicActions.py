import time
import re
from appium.webdriver.webelement import WebElement

from selenium.common.exceptions import NoSuchElementException

from BasePage import BasePage


class BasicActions(BasePage):
    '''
    Parent class with basic actions for any PageObject actions class
    '''
    def _send_keys(self, value: str, element: WebElement) -> None:
        element.clear()
        element.send_keys(value)
        self._hide_keyboard()

    def _click_on(self, element: WebElement) -> None:
        self._hide_keyboard()
        try:
            element.click()
        except AttributeError:
            self.action.tap(None, element.location['x'] + element.size['width'] / 2, element.location['y']
                            + element.size['height'] / 2, 1).perform()

    def _hide_keyboard(self) -> None:
        if self.driver.is_keyboard_shown():
            self.driver.hide_keyboard()


    @staticmethod
    def _get_float_from_string(text: str) -> float:
        return float(re.findall(r"[-+]?\d*\.\d+|\d+", text)[0])

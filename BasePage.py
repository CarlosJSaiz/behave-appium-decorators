import time
from typing import Callable, List
from appium import webdriver

from appium.webdriver import WebElement
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import WebDriverException


def element_loop(max_attempts, element_display_timer):
    '''
    Creates a decorator to loop for element location.
    '''
    def real_decorator(function):
        def wrapper(args):
            attempt = 0
            result = None
            while max_attempts > attempt and result not in [WebElement, List]:
                if max_attempts == attempt:
                    raise WebDriverException("Element not found")
                try:
                    result = function(args)
                    if result not in [WebElement, List]:
                        time.sleep(element_display_timer)
                        attempt = attempt + 1
                except IndexError:
                    time.sleep(element_display_timer)
                    attempt = attempt + 1
            return result
        return wrapper
    return real_decorator


class BasePage:
    '''
    Parent class with basic information for any PageObject
    '''
    platform = "None"

    def __init__(self, driver, bottom_limit_factor=0.95, upper_limit_factor=0.05):
        self.driver = driver
        self.action = TouchAction(self.driver)
        self.wait = WebDriverWait(self.driver, 20)
        self.EC = expected_conditions
        BasePage.platform = self.driver.desired_capabilities['platformName']
        self.device_width = self.driver.get_window_size()['width']
        self.device_height = self.driver.get_window_size()['height']
        self.bottom_limit = self.device_height * bottom_limit_factor
        self.upper_limit = self.device_height * upper_limit_factor

    def __get_platform(self) -> str:
        return self.platform

    def get_driver(self) -> webdriver:
        return self.driver

    def android_platform(self) -> bool:
        if self.__get_platform() == "android":
            return True
        else:
            return False

    def ios_platform(self) -> bool:
        if self.__get_platform() == "iOS":
            return True
        else:
            return False

    @staticmethod
    @element_loop(max_attempts=10, element_display_timer=0.5)
    def get_element(selector_and_method: "tuple[str, Callable]") -> WebElement:
        return selector_and_method[1](selector_and_method[0])[0]

    @staticmethod
    @element_loop(max_attempts=10, element_display_timer=0.5)
    def get_elements(selector_and_method: "tuple[str, Callable]") -> WebElement:
        return selector_and_method[1](selector_and_method[0])

    def element_is_present(self, selector_and_method: "tuple[str, Callable]") -> bool:
        if len(self.get_elements(selector_and_method)) == 0:
            return False
        else:
            return True

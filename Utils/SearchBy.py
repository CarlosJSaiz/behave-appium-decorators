from BasePage import BasePage
from typing import Callable, Literal, Union

ByTypeAndroid = Literal['text', 'xpath', 'class_name',
                        'uiautomator', 'resource-id', 'name']
ByTypeIos = Literal['text', 'xpath', 'class_name',
                    'ios_class', 'ios_predicate', 'accessibility_id', 'name']
ByType = Union[ByTypeAndroid, ByTypeIos]

ANDROID_PACKAGE = "com.swaglabsmobileapp"
ANDROID_ID_PRE = 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().resourceId("' + \
    ANDROID_PACKAGE + ':id/'
ANDROID_TEXT_PRE = 'new UiScrollable(new UiSelector()).scrollTextIntoView("'
ANDROID_TEXT_POST = '")'
ANDROID_ID_POST = '"))'


class Finder(BasePage):
    '''
    Creates a decorator to define selector and selector type for locate an elemente in Android and iOS.
    '''

    def __init__(self, driver):
        super().__init__(driver)

    @classmethod
    def element(cls, ios_by: ByTypeIos, ios_locator: str, android_by: ByTypeAndroid, android_locator: str) -> "tuple[str, Callable]":
        def real_decorator(function):
            def wrapper(*args):
                if cls.platform == "iOS":
                    by: ByTypeIos = ios_by
                    locator: str = ios_locator
                elif cls.platform == "android":
                    by: ByTypeAndroid = android_by
                    locator: str = android_locator
                else:
                    raise ValueError("Platform is not defined")
                if by and locator:
                    return function(*args, by, locator)
            return wrapper
        return real_decorator


class SearchBy(BasePage):
    ''' Asign a location method and complete the selector'''

    def __find_by_android(self, by: ByTypeAndroid, selector: str) -> "tuple[str, Callable]":
        '''
        Parameters
        ----------
        by : ByTypeAndroid
            Type of selector
        Selector : str
            Selector string

        Returns
        ----------
            Selector: str
                Final selector for element
            Method: Callable
                Method to locate element
        '''
        if by == 'text':
            return ANDROID_TEXT_PRE + selector + ANDROID_TEXT_POST, self.driver.find_elements_by_android_uiautomator
        elif by == 'xpath':
            return selector, self.driver.find_elements_by_xpath
        elif by == 'class_name':
            return selector, self.driver.find_elements_by_class_name
        elif by == 'uiautomator':
            return ANDROID_ID_PRE + selector + ANDROID_ID_POST, self.driver.find_elements_by_android_uiautomator
        elif by == 'resource-id':
            return ANDROID_PACKAGE + ":id/" + selector, self.driver.find_elements_by_id

    def __find_by_ios(self, by: ByTypeIos, selector: str) -> "tuple[str, Callable]":
        '''
        Parameters
        ----------
        by : ByTypeAndroid
            Type of selector
        Selector : str
            Selector string

        Returns
        ----------
            Selector: str
                Final selector for element
            Method: Callable
                Method to locate element
        '''
        if by == 'ios_class':
            return selector, self.driver.find_elements_by_class_name
        elif by == 'ios_predicate':
            return selector, self.driver.find_elements_by_ios_predicate
        elif by == 'accessibility_id':
            return selector, self.driver.find_elements_by_accessibility_id
        elif by == 'name':
            return "name CONTAINS '" + selector + "'", self.driver.find_elements_by_ios_predicat
        elif by == 'xpath':
            return selector, self.driver.find_elements_by_xpath
        elif by == 'text':
            return 'wdLabel LIKE "' + selector + '"', self.driver.find_elements_by_ios_predicate

    def find_by(self, by: ByType, selector: str) -> "tuple[str, Callable]":
        if self.android_platform():
            return self.__find_by_android(by, selector)
        elif self.ios_platform():
            return self.__find_by_ios(by, selector)

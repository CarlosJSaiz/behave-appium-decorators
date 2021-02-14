from typing import Callable
from .LoginScreenBase import LoginScreenBase
from Utils.SearchBy import SearchBy, Finder
from appium.webdriver.webelement import WebElement


class LoginScreenElements(SearchBy, LoginScreenBase):
    @Finder.element(ios_by="accessibility_id",
                    ios_locator="test-Login",
                    android_by="xpath",
                    android_locator="//android.widget.ScrollView[@content-desc=\"test-Login\"]")
    def login_screen_selector(self, *args) -> "tuple[str, Callable]":
        return self.find_by(*args)

    @Finder.element(ios_by="accessibility_id",
                    ios_locator="test-Username",
                    android_by="xpath",
                    android_locator="//android.widget.EditText[@content-desc=\"test-Username\"]")
    def username_field_selector(self, *args) -> "tuple[str, Callable]":
        return self.find_by(*args)

    @Finder.element(ios_by="accessibility_id",
                    ios_locator="test-Password",
                    android_by="xpath",
                    android_locator="//android.widget.EditText[@content-desc=\"test-Password\"]")
    def password_field_selector(self, *args) -> "tuple[str, Callable]":
        return self.find_by(*args)

    @Finder.element(ios_by="accessibility_id",
                    ios_locator="test-LOGIN",
                    android_by="xpath",
                    android_locator="//android.view.ViewGroup[@content-desc=\"test-LOGIN\"]")
    def login_button_selector(self, *args) -> "tuple[str, Callable]":
        return self.find_by(*args)

    def get_username_field_element(self) -> WebElement:
        return self.get_element(self.username_field_selector())

    def get_password_field_element(self) -> WebElement:
        return self.get_element(self.password_field_selector())

    def get_login_button_element(self) -> WebElement:
        return self.get_element(self.login_button_selector())

    def get_login_screen_element(self) -> WebElement:
        return self.get_element(self.login_screen_selector())

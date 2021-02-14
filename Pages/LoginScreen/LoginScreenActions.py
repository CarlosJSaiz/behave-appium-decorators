from Utils import BasicActions
from .LoginScreenBase import LoginScreenBase
from .LoginScreenElements import LoginScreenElements


class LoginScreenActions(BasicActions, LoginScreenBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.elements = LoginScreenElements(driver)

    def __insert_username(self, text: str) -> None:
        self._send_keys(text, self.elements.get_username_field_element())

    def __insert_password(self, text: str) -> None:
        self._send_keys(text, self.elements.get_password_field_element())

    def __tap_on_login_button(self) -> None:
        self._click_on(self.elements.get_login_button_element())

    def login(self, username: str, password: str) -> None:
        self.__insert_username(username)
        self.__insert_password(password)
        self.__tap_on_login_button()

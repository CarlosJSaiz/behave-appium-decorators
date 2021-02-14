from .LoginScreenBase import LoginScreenBase
from .LoginScreenElements import LoginScreenElements


class LoginScreenAsserts(LoginScreenBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.elements = LoginScreenElements(driver)

    def login_screen_is_displayed(self) -> None:
        assert self.element_is_present(
            self.elements.login_screen_selector()), "Login Screen is not displayed"

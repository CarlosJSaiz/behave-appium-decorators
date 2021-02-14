from BasePage import BasePage


class ProductsScreenBase(BasePage):
    def __init__(self, driver):
        super().__init__(driver, upper_limit_factor=0.2)

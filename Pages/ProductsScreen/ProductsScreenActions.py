from typing import NoReturn

from Utils import BasicActions
from .ProductsScreenBase import ProductsScreenBase
from .ProductsScreenElements import ProductsScreenElements


class ProductsScreenActions(BasicActions, ProductsScreenBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.elements = ProductsScreenElements(driver)

    def get_price_float_from_text(self) -> float:
        return self._get_float_from_string(self.elements.get_baby_tshirt_price_element().text)

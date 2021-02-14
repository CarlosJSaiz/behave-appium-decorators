from Pages.ProductsScreen.ProductsScreenActions import ProductsScreenActions
from .ProductsScreenBase import ProductsScreenBase
from .ProductsScreenElements import ProductsScreenElements


class ProductsScreenAsserts(ProductsScreenBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.elements = ProductsScreenElements(driver)
        self.actions = ProductsScreenActions(driver)

    def products_screen_is_displayed(self) -> None:
        assert self.element_is_present(
            self.elements.products_screen_selector()), "Products Screen is not displayed"

    def check_price_is_correct(self, price: str) -> None:
        assert self.actions.get_price_float_from_text() == float(
            price), "Price is not as expected"

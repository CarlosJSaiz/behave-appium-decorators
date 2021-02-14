from Utils import ScrollAndSwipe
from .ProductsScreenBase import ProductsScreenBase
from .ProductsScreenElements import ProductsScreenElements


class ProductsScreenScrolls(ScrollAndSwipe, ProductsScreenBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.elements = ProductsScreenElements(driver)

    def put_on_viemport_baby_tshirt(self) -> None:
        self.put_selector_on_viewport(
            self.elements.baby_tshirt_product_selector(), 'Down')

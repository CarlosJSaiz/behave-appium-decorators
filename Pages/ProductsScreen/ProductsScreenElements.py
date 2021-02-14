from typing import Callable

from appium.webdriver.webelement import WebElement
from .ProductsScreenBase import ProductsScreenBase
from Utils.SearchBy import SearchBy, Finder



class ProductsScreenElements(SearchBy, ProductsScreenBase):
    @Finder.element(ios_by="accessibility_id",
                    ios_locator="test-PRODUCTS",
                    android_by="xpath",
                    android_locator="//android.widget.ScrollView[@content-desc=\"test-PRODUCTS\"]")
    def products_screen_selector(self, *args) -> "tuple[str, Callable]":
        return self.find_by(*args)

    @Finder.element(ios_by="text",
                    ios_locator="Sauce Labs Onesie",
                    android_by="text",
                    android_locator="Sauce Labs Onesie")
    def baby_tshirt_product_selector(self, *args) -> "tuple[str, Callable]":
        return self.find_by(*args)

    @Finder.element(ios_by="xpath",
                    ios_locator="//XCUIElementTypeStaticText[@label=\"Sauce Labs Onesie\"]/ancestor::XCUIElementTypeOther[1]/following-sibling::XCUIElementTypeOther/XCUIElementTypeStaticText",
                    android_by="xpath",
                    android_locator="//*[@text=\"Sauce Labs Onesie\"]/following-sibling::*[@content-desc=\"test-Price\"]")
    def baby_tshirt_price_selector(self, *args) -> "tuple[str, Callable]":
        return self.find_by(*args)

    def get_products_screen_element(self) -> WebElement:
        return self.get_element(self.products_screen_selector())

    def get_baby_tshirt_product_element(self) -> WebElement:
        return self.get_element(self.baby_tshirt_product_selector())

    def get_baby_tshirt_price_element(self) -> WebElement:
        return self.get_element(self.baby_tshirt_price_selector())

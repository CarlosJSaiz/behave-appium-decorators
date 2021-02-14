from typing import Callable, Literal

from BasePage import BasePage

DirectionType = Literal['Up', 'Down']


class ScrollAndSwipe(BasePage):
    '''
    Handles any scroll and swipe actions.
    '''

    def put_selector_on_viewport(self, selector_and_method: "tuple[str, Callable]", direction: DirectionType, scroll_ratio:float = 0.2, max_attempts: int = 10):
        '''
        Parameters
        ----------
        selector_and_method : tuple[str, Callable]
            Selector String and method to locate element
        direction : DirectionType
            Can be 'Up' and 'Down'
        scroll_ratio? : int
            Speed of every scroll step
        max_attempts? : int
            Numbers of scroll steps until error
        '''
        selector: str = selector_and_method[0]
        method: Callable = selector_and_method[1]
        attempt: int = 0
        direction_scroll = self.__get_direction_scroll(direction)
        while len(method(selector)) == 0 and attempt < max_attempts:
            direction_scroll(scroll_ratio)
            attempt += 1
        if len(method(selector)) == 0:
            raise ValueError(selector+' is not displayed')
        element = method(selector)[0]
        while not self.upper_limit < element.location['y'] < self.bottom_limit and attempt < max_attempts:
            direction_scroll(scroll_ratio)
            element = method(selector)[0]
            attempt += 1
            if attempt == max_attempts:
                raise ValueError(selector+' is not displayed')

    def __get_direction_scroll(self, direction: DirectionType) -> Callable:
        if direction == 'Down':
            return self.__scroll_down
        elif direction == 'Up':
            return self.__scroll_up

    def __scroll_down(self, scroll_ratio:float) -> None:
        if self.android_platform():
            self.__android_scroll_down(scroll_ratio)
        elif self.ios_platform():
            self.__ios_scroll_down(scroll_ratio)

    def __scroll_up(self, scroll_ratio:float) -> None:
        if self.android_platform():
            self.__android_scroll_up(scroll_ratio)
        elif self.ios_platform():
            self.__ios_scroll_up(scroll_ratio)

    def __ios_scroll_down(self, scroll_ratio:float) -> None:
        self.action.long_press(x=self.device_width / 2,
                               y=self.device_height / 2).move_to(x=self.device_width / 2,
                                                                 y=self.device_height * scroll_ratio).release().perform()

    def __ios_scroll_up(self, scroll_ratio:float) -> None:
        self.action.long_press(x=self.device_width / 2,
                               y=self.device_height * scroll_ratio).move_to(x=self.device_width / 2,
                                                                            y=self.device_height / 2).release().perform()

    def __android_scroll_down(self, scroll_ratio:float) -> None:
        x1 = str(self.device_width / 2)
        y1 = str(self.device_height / 2)
        x2 = str(self.device_width / 2)
        y2 = str(self.device_height * scroll_ratio)
        self.driver.execute_script('mobile: shell', {
            'command': 'input swipe',
            'args': [x1, y1, x2, y2],
            'includeStderr': True,
            'timeout': 5000
        })

    def __android_scroll_up(self, scroll_ratio:float) -> None:
        x1 = str(self.device_width / 2)
        y1 = str(self.device_height * scroll_ratio)
        x2 = str(self.device_width / 2)
        y2 = str(self.device_height / 2)
        self.driver.execute_script('mobile: shell', {
            'command': 'input swipe',
            'args': [x1, y1, x2, y2],
            'includeStderr': True,
            'timeout': 5000
        })

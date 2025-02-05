import time

import allure
from Object_Repository import Selenium_4_pop_up_OR
from Selenium_Operations.Element_Operations import Element_Operations


class Selenium_4_Popup_Page(Element_Operations):

    def __init__(self, driver):
        self.driver = driver
        Element_Operations.__init__(self, self.driver)

    @allure.step("Close Selenium 4 Pop Up")
    def close_selenium_four_popup(self):
        self.set_fullscreen_window()
        self.wait_until_element_present_visible(Selenium_4_pop_up_OR.Selenium4_popup_close_icon)
        self.click(Selenium_4_pop_up_OR.Selenium4_popup_close_icon)

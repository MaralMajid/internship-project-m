from pages.base_page import Page
from pages.web_app_page import Web_App_Page
from pages.sing_in_page import Sign_In_Page
from pages.main_page import Main_Page
from pages.reelly_setting_page import SettingPage
from pages.reelly_fltr_want_to_buy_page import FltrWantToBuy
from pages.reelly_secondary_price_page import SecondaryPricePage

class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.web_app_page = Web_App_Page(driver)
        self.sign_in_page = Sign_In_Page(driver)
        self.main_page = Main_Page(driver)
        self.reelly_setting_page = SettingPage(driver)
        self.reelly_fltr_want_to_buy_page = FltrWantToBuy(driver)
        self.reelly_secondary_price_page = SecondaryPricePage(driver)




from pages.base_page import Page
from pages.web_app_page import Web_App_Page
from pages.sing_in_page import Sign_In_Page
from pages.main_page import Main_Page
from pages.reelly_setting_page import SettingPage

class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.web_app_page = Web_App_Page(driver)
        self.sign_in_page = Sign_In_Page(driver)
        self.main_page = Main_Page(driver)
        self.reelly_setting_page = SettingPage(driver)



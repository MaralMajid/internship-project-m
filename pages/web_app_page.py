from pages.base_page import Page
from selenium.webdriver.common.by import By



class Web_App_Page(Page):
    SIGN_IN_BTTN= (By.CSS_SELECTOR, "[class='sing-in-text']")
    def open(self):
        self.open_url('https://soft.reelly.io/sign-up')

    def click(self):
        self.driver.find_element(*self.SIGN_IN_BTTN).click()

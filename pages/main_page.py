from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep



class Main_Page(Page):
    TEXT_VRFY = (By.XPATH,"//*[contains(text(),'Total projects')]")
    def verify_msg (self, *locator):
        sleep(4)
        self.verify_text('Total projects', *self.TEXT_VRFY)

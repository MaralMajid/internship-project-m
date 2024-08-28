from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.keys import Keys


class Sign_In_Page(Page):
    USERNAME_INPUT = (By.CSS_SELECTOR,"[wized='emailInput']")
    PASSWORD_INPUT = (By.CSS_SELECTOR,"[wized='passwordInput']")
    CONTINUE_BTTN = (By.CSS_SELECTOR, "[wized='loginButton']")



    def input_email(self, *locator):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys('maralmajid94@gmail.com')

    def input_password(self, *locator):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys('abcfed132')

    def click(self, *locator):
        self.driver.find_element(*self.CONTINUE_BTTN).click()
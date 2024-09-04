from selenium.webdriver.common.keys import Keys
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class SettingPage(Page):
    SETTING_BTTN= (By.CSS_SELECTOR,"a[href='/settings']")
    USER_GUIDE_BTN= (By.CSS_SELECTOR,'a[href="/user-guide"] div[class="setting-text"]')
    USER_GUIDE_PAGE=(By.XPATH,"//*[contains(text(),'User guide')]")
    VIDEO_TITLE = (By.CSS_SELECTOR, '#player div[class*=cards-title]')
    VID_IFRAME = (By.CSS_SELECTOR, ".embedly-embed")
    SEC_IFRAME = (By.ID, "player")


    def click_setting_button(self,*locator):
        sleep(5)
        self.click(*self.SETTING_BTTN)

    def click_user_guide_btn(self,*locator):
        self.click(*self.USER_GUIDE_BTN)


    # def verify_right_page(self):
    #     self.driver.find_element(*self.USER_GUIDE_PAGE)

    def verify_right_url(self):
        self.verify_url('https://soft.reelly.io/user-guide')


    def verify_video_title(self):
        iframe_element = self.find_element(*self.VID_IFRAME)
        self.driver.switch_to.frame(iframe_element)
        second_iframe = self.find_element(*self.SEC_IFRAME)
        self.driver.switch_to.frame(second_iframe)
        self.wait.until(EC.presence_of_element_located(self.VIDEO_TITLE))
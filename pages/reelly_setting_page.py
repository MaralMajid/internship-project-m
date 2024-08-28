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
    VIDEO_TITLE= (By.CSS_SELECTOR, 'div[class="ytp-title"]')


    def click_setting_button(self,*locator):
        self.click(*self.SETTING_BTTN)

    def click_user_guide_btn(self,*locator):
        self.click(*self.USER_GUIDE_BTN)


    def verify_right_page(self):
        self.driver.find_element(*self.USER_GUIDE_PAGE)


    def verify_video_title(self):
        sleep(10)
        self.find_element(*self.VIDEO_TITLE)

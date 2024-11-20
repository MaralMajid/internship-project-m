from selenium.webdriver.common.keys import Keys
from pages.base_page import Page
from pages.reelly_fltr_want_to_buy_page import FltrWantToBuy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



class OffPlanPricePage(Page):
    OffPlan=(By.CSS_SELECTOR,'a[href="/"]')
    FILTER=(By.CSS_SELECTOR, 'a[class="filter-button w-inline-block"]')
    def click_off_plan(self):
        self.click(*self.OffPlan)


    def verify_right_url(self):
        self.verify_url('https://soft.reelly.io/')


    def click_on_filter(self, *locator):
        sleep(3)
        self.wait_for_element_to_be_clickable_click(*self.FILTER)
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains



class FltrWantToBuy(Page):
    SCNDRY_OPTION=(By.XPATH,"//a[contains(@href,'/secondary-listings')]")
    FILTERS= (By.CSS_SELECTOR, "div[class='filter-button']")
    SLCT_WANT_TO_BUY= (By.CSS_SELECTOR,'div[class="switcher-button active"]')
    APPLY_FILTER= (By.XPATH,'//a[text()="Apply filter"]')
    ALL_CARD_TAGS=(By.CSS_SELECTOR,'//div[text()="Want to buy"]')



    def click_on_secondary_option_menu(self,*locator):
        self.click(*self.SCNDRY_OPTION)


    def verify_right_page_opens(self):
        self.verify_url('https://soft.reelly.io/secondary-listings')



    def click_on_filters(self, *locator):
        #self.click(*self.FILTERS)
        sleep(3)
        self.wait_for_element_to_be_clickable_click(*self.FILTERS)



    def select_want_to_buy(self, *locator):
        self.driver.find_element(*self.SLCT_WANT_TO_BUY).click()


    def click_apply_filter(self,*locator):
        self.click(*self.APPLY_FILTER)
        sleep(2)



    def all_card_tags(self):
        driver=self.driver
        wait= WebDriverWait(driver, 10)
        cards= driver.find_elements(By.CSS_SELECTOR,'div[wized="saleTagMLS"]')

        all_have_tag = True

        for card in cards:
            try:
                want_to_buy_tag = card.find_elements(By.XPATH, '//div[text()="Want to buy"]')
                print("Tag found in card:", card)
            except NoSuchElementException:
                print("Tag not found in one of the cards:" , card)
                all_have_tag = False

        if all_have_tag:
            print("All cards contain the 'Want to buy' tag.")
        else:
            print("Some cards do not contain the 'Want to buy' tag.")
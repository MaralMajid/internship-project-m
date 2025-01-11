from selenium.webdriver.common.keys import Keys
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



class OutOfStockPage(Page):

    SALE_STATUS = (By.CSS_SELECTOR,'select[wized="saleStatusFilter"]')
    OUT_OF_STOCK = (By.CSS_SELECTOR,'option[value="Out of stock"]')


    def click_on_sale_status(self, *locator):
        self.click(*self.SALE_STATUS)



    def click_on_out_of_stock(self, *locator):
        self.click(*self.OUT_OF_STOCK)



    def verify_tags(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        out_of_stock_tag = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[wized=projectStatus]")))
        assert "Out of stock" in out_of_stock_tag.text, "The tag does not contain 'Out of stock'"
        print("The tag contains 'Out of stock'")

from selenium.webdriver.common.keys import Keys
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class PicTitleVisibilityPage(Page):
    def pic_and_title_visible(self):
        products = self.find_elements(By.CSS_SELECTOR, 'div[wized="projectsListing"]')
        for product in products:
            title =product.find_element(By.CSS_SELECTOR, 'div[wized="projectName"]')
            picture =product.find_element(By.CSS_SELECTOR,'div[wized="projectImage"]')
            sleep(7)

            assert title.is_displayed(), f"Title not visible for product: {product.text}"
            assert picture.is_displayed(), f"Picture not visible for product: {product.text}"

        print("All products have visible titles and pictures.")
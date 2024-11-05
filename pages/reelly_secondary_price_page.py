from selenium.webdriver.common.keys import Keys
from pages.base_page import Page
from pages.reelly_fltr_want_to_buy_page import FltrWantToBuy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



class SecondaryPricePage(Page):
    PRICE_FROM=(By.CSS_SELECTOR,'input[wized="unitPriceFromFilter"]')
    PRICE_TO=(By.CSS_SELECTOR, 'input[wized="unitPriceToFilter"]')
    NMBR_PRC_TXT=(By.CSS_SELECTOR,'div[class="number-price-text"]')

    def price_filter_from(self):
        self.driver.execute_script("window.scrollBy(0, 510)")
        self.input_text(1200000, *self.PRICE_FROM)

    def price_filter_to(self):
        self.input_text(2000000, *self.PRICE_TO)


    def verify_price_range(self):
       cards= self.find_elements(*self.NMBR_PRC_TXT)
       all_prices_in_range = True
       for card in cards:
           price_text =card.text
           try:
               price = int(price_text.replace('AED'," ").replace(',' ,'').strip())
           except ValueError:
               print(f'Could not convert price: {price_text}')
               all_prices_in_range = False
               continue
           if 1200000 < price< 2000000:
               print(f'Price {price} AED is within range.')
           else:
               print(f'Price {price} AED is out of range.')
               all_prices_in_range = False

       if all_prices_in_range:
           print("All product prices are within the specified range.")
       else:
           print("Some product prices are out of the specified range.")

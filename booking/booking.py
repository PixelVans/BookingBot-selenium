import booking.constants as const
import os
import time
from selenium import webdriver
from booking.booking_filtration import BookingFiltration
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers",
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(45)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        time.sleep(2)
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()

        selected_currency_element = self.find_element(By.XPATH, f'//div[contains(@class, "CurrencyPicker_currency") and text()="{currency}"]')
        selected_currency_element.click()


    def select_place_to_go(self, place_to_go):
        time.sleep(2)
        search_field = self.find_element(By.NAME, "ss")
        search_field.clear()
        search_field.send_keys(place_to_go)
        time.sleep(4)
        first_result = self.find_element(By.ID, 'autocomplete-result-1')
        time.sleep(2)
        first_result.click()
        

    def select_dates(self, check_in_date, check_out_date):
        time.sleep(2)
        check_in_element = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_in_date}"]')
        check_in_element.click()
        
        time.sleep(1)

        check_out_element = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
        check_out_element.click()



    def select_adults(self, adults=1): 
        selection_button = self.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
        selection_button.click()
        time.sleep(1)  # Allow dropdown to open

        adults_value_element = self.find_element(By.CSS_SELECTOR, 'span.d723d73d5f')
        current_adults = int(adults_value_element.text)

        increase_button = self.find_element(By.CSS_SELECTOR, 'button.bb803d8689.f4d78af12a')  # Increase button
        decrease_button = self.find_element(By.CSS_SELECTOR, 'button.bb803d8689.e91c91fa93')  # Decrease button

        # Reduce adults to 1 before increasing
        while current_adults > 1:
            decrease_button.click()
            time.sleep(0.5)
            current_adults -= 1

        # Increase adults to the desired number
        while current_adults < adults:
            increase_button.click()
            time.sleep(1)
            current_adults += 1

        # Close the dropdown by clicking the selection button again
        selection_button.click()


    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR,
            'button[type="submit"]'
        )
        search_button.click()
        
        
    def close_modal_if_present(self):
        try:
            close_button = self.find_element(By.CSS_SELECTOR, 'button.f4552b6561')
            close_button.click()
            time.sleep(2)  # Wait briefly to ensure the modal closes
            print("Modal closed successfully.")
        except NoSuchElementException:
            print("Modal not found, continuing...")

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(4, 5)

        filtration.sort_price_lowest_first()
        
        

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        # Locate the star rating filter container
        star_filtration_box = self.driver.find_element(By.ID, 'filter_group_class_:r31:')
        
        # Get all child elements within the filter container
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')

        # Loop through the given star values and click the corresponding filter option
        for star_value in star_values:
            for star_element in star_child_elements:
                if star_element.get_attribute('innerHTML').strip() == f'{star_value} stars':
                    star_element.click()
                    break  # Click once and stop checking further for this star value

    def sort_price_lowest_first(self):
        # Locate and click the price sorting filter
        element = self.driver.find_element(By.CSS_SELECTOR, 'li[data-id="price"]')
        element.click()

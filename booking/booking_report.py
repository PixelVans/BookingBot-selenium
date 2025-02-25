from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class BookingReport:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        """Fetch all deal boxes within the provided section."""
        return self.boxes_section_element.find_elements(By.CLASS_NAME, "sr_property_block")

    def pull_deal_box_attributes(self):
        """Extract hotel name, price, and score from each deal box."""
        collection = []
        for deal_box in self.deal_boxes:
            try:
                hotel_name = deal_box.find_element(By.CLASS_NAME, "sr-hotel__name").text.strip()
                hotel_price = deal_box.find_element(By.CLASS_NAME, "bui-price-display__value").text.strip()
                hotel_score = deal_box.get_attribute("data-score").strip() or "N/A"  # Handle missing scores

                collection.append([hotel_name, hotel_price, hotel_score])

            except Exception as e:
                print(f"Error extracting data from a deal box: {e}")
                continue  # Skip this box if there's an issue

        return collection

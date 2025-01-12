from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class NovaPoshtaTrackingTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = "https://tracking.novaposhta.ua/#/uk"

    def test_tracking_status(self):
        driver = self.driver
        driver.get(self.url)

        tracking_number = "20400123456789"
        expected_status = "Посилка отримана"

        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Введіть номер накладної']"))
        )
        input_field.send_keys(tracking_number + Keys.RETURN)

        status_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header__status-text"))
        )

        actual_status = status_element.text

        self.assertEqual(expected_status, actual_status, f"Очікувався статус '{expected_status}', але отримано '{actual_status}'")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

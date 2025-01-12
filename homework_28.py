import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://guest:welcome2qauto@qauto2.forstudy.space"

# PageObjects
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.register_button = (By.XPATH, "//button[contains(text(), 'Register')]")

    def go_to_registration_page(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.register_button)).click()

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "user_first_name")
        self.last_name_input = (By.ID, "user_last_name")
        self.email_input = (By.ID, "user_email")
        self.password_input = (By.ID, "user_password")
        self.confirm_password_input = (By.ID, "user_password_confirmation")
        self.register_button = (By.XPATH, "//button[contains(text(), 'Sign up')]")

    def fill_registration_form(self, first_name, last_name, email, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_name_input)).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.confirm_password_input).send_keys(password)

    def submit_registration(self):
        self.driver.find_element(*self.register_button).click()

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_message = (By.XPATH, "//h1[contains(text(), 'Welcome')]")

    def is_welcome_message_displayed(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.welcome_message)) is not None

# Фікстури
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)

@pytest.fixture
def dashboard_page(driver):
    return DashboardPage(driver)

@pytest.mark.parametrize("first_name, last_name, email, password", [
    ("Test", "User", "testuser@example.com", "Password123")
])
def test_user_registration(driver, home_page, registration_page, dashboard_page, first_name, last_name, email, password):
    home_page.go_to_registration_page()

    registration_page.fill_registration_form(first_name, last_name, email, password)

    registration_page.submit_registration()

    assert dashboard_page.is_welcome_message_displayed(), "Welcome message was not displayed after registration"

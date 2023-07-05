from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self, base_url):
        self.driver.get(base_url)

    def click_login_button(self):
        try:
            register_link = self.driver.find_element(By.XPATH,
                                                     '//*[@id="__next"]/div/div/div[2]/div[2]/div/div/div[2]/a')
            register_link.click()
        except NoSuchElementException:
            raise Exception("Login link not found")

    def enter_username(self, username):
        try:
            username_input = self.driver.find_element(By.NAME, "email")
            username_input.send_keys(username)
        except NoSuchElementException:
            raise Exception("Username input field not found")

    def enter_password(self, password):
        try:
            password_input = self.driver.find_element(By.NAME, "password")
            password_input.send_keys(password)
        except NoSuchElementException:
            raise Exception("Password input field not found")

    def submit_login_form(self):
        try:
            submit_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="login-submit-button"]')
            submit_button.click()
        except NoSuchElementException:
            raise Exception("Login button not found")

    def is_password_error_message_displayed(self):
        try:
            error_message = self.driver.find_element(By.CSS_SELECTOR,
                                                     'p[data-testid="login-password-input-error"]').text
            return error_message
        except NoSuchElementException:
            return None

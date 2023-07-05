import os
import unittest

from parameterized import parameterized

from utils.base import BaseTestCase
from pages.login import LoginPage


class NegativeLoginTestCase(BaseTestCase):
    @parameterized.expand([
        ("invalid_username@gmail.com", "invalid_password", os.getenv('url')),
        ("invalid_username@gmail.com", "valid_password", os.getenv('url')),
        ("valid_username@gmail.com", "another_invalid_password", os.getenv('url')),
    ])
    def test_negative_login(self, username, password, url):
        login_page = LoginPage(self.driver)
        login_page.load(url)
        login_page.click_login_button()
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.submit_login_form()
        messages = login_page.load_messages()
        self.assertEqual(login_page.is_password_error_message_displayed(), messages['invalid_login_error_message'])


if __name__ == '__main__':
    unittest.main()
import unittest

from parameterized import parameterized

from utils.base import BaseTestCase
from pages.login import LoginPage

base_url = "https://www.limango.pl/"


class NegativeLoginTestCase(BaseTestCase):
    @parameterized.expand([
        ("invalid_username@gmail.com", "invalid_password", base_url),
        ("invalid_username@gmail.com", "valid_password", base_url),
        ("valid_username@gmail.com", "another_invalid_password", base_url),
    ])
    def test_negative_login(self, username, password, url):
        login_page = LoginPage(self.driver)
        login_page.load(url)
        login_page.click_login_button()
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.submit_login_form()


if __name__ == '__main__':
    unittest.main()

import unittest
import chromedriver_autoinstaller

from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
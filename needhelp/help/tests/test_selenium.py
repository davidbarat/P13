# import selenium
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys


class grandPyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(
            "/Users/david/Projets/selenium driver/")
        self.url = "http://127.0.0.1:8000/"

    def test_search(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.elem = self.driver.find_element_by_id("inputSearch")
        self.elem.send_keys(self.search)
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

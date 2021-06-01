# import selenium
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys


class needHelpTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(
            "/Users/david/Projets/selenium driver/")
        self.url = "http://127.0.0.1:8000/"
        self.user = 'test@test.com'
        self.password = '007Test!'
        self.id_Nom = 'Test'
        self.id_Email = 'test@test.te'
        self.id_Mobile = '0607080910'
        self.id_Message = 'ceci est un test'

    def test_link_home(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.elem = self.driver.find_element_by_id("about")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.elem = self.driver.find_element_by_id("home")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.elem = self.driver.find_element_by_id("faq")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)

    def test_login(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.elem = self.driver.find_element_by_id("login")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.elem = self.driver.find_element_by_id("id_username")
        self.elem.send_keys(self.user)
        self.elem = self.driver.find_element_by_id("id_password")
        self.elem.send_keys(self.password)
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)

    def test_contact(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.elem = self.driver.find_element_by_id("contact")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.elem = self.driver.find_element_by_id("id_Nom")
        self.elem.send_keys(self.id_Nom)
        self.elem = self.driver.find_element_by_id("id_Email")
        self.elem.send_keys(self.id_Email)
        self.elem = self.driver.find_element_by_id("id_Mobile")
        self.elem.send_keys(self.id_Mobile)
        self.elem = self.driver.find_element_by_id("id_Message")
        self.elem.send_keys(self.id_Message)
        self.elem = self.driver.find_element_by_id("send")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

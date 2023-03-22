import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class websiteTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://demostore.supersqa.com")
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 20)

    def test_cart(self):
        self.cart = self.driver.find_element(
            By.XPATH, "(//a[normalize-space()='Cart'])[1]")
        self.cart.click()
        expected_cart_text = "Your cart is currently empty."
        text_cart = self.driver.find_element(
            By.CSS_SELECTOR, ".cart-empty.woocommerce-info").text

        self.assertEqual(expected_cart_text, text_cart)

    def test_add_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label='Add “Album” to your cart']")))
        self.driver.find_element(
            By.CSS_SELECTOR, "a[aria-label='Add “Album” to your cart']").click()
        self.wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "a[title='View your shopping cart'] span[class='woocommerce-Price-amount amount']"), "$15.00"))
        cart = self.driver.find_element(
            By.CSS_SELECTOR, "a[title='View your shopping cart']")
        cart.click()
        product = self.driver.find_element(
            By.CSS_SELECTOR, "td[class='product-name']").text
        actual = "Album"

        self.assertEqual(product, actual)

    def test_remove_from_cart(self):
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label='Add “Album” to your cart']")))
        self.driver.find_element(
            By.CSS_SELECTOR, "a[aria-label='Add “Album” to your cart']").click()
        self.wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "a[title='View your shopping cart'] span[class='woocommerce-Price-amount amount']"), "$15.00"))
        self.driver.find_element(
            By.CSS_SELECTOR, "a[title='View your shopping cart']").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "a[aria-label='Remove this item']").click()
        actual = self.driver.find_element(
            By.CSS_SELECTOR, "div[role='alert']").text
        expected = "“Album” removed. Undo?"

        self.assertEqual(actual, expected)

    def test_login_wrong_credintials(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9 > a").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#username").send_keys("atef")
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys("123")
        self.driver.find_element(
            By.CSS_SELECTOR, "button[value='Log in']").click()
        actual = self.driver.find_element(
            By.CSS_SELECTOR, "#content > div > div.woocommerce > ul > li").text
        expected = "Error: The username atef is not registered on this site. If you are unsure of your username, try your email address instead."

        self.assertEqual(expected, actual)

    def test_login_credintials(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9 > a").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#username").send_keys("atefm6@outlook.com")
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys("A9517538624m")
        self.driver.find_element(
            By.CSS_SELECTOR, "button[value='Log in']").click()
        actual = self.driver.find_element(
            By.CSS_SELECTOR, "div[id='content'] strong:nth-child(1)").text
        expected = "atefm6"

        self.assertEqual(expected, actual)

    def tearDown(self) -> None:
        self.driver.close()

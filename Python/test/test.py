import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.basics import Basics
from utils.selectors import Selectors


class Exercise(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")

        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
        self.driver.get("https://www.saucedemo.com/")

        self.basics = Basics(self.driver)

    def log_in_with_standard_user_account(self):
        self.basics.clear_element(Selectors.username_textfield)
        self.basics.send_text_to_element(Selectors.username_textfield, "standard_user")
        self.basics.clear_element(Selectors.username_passwordfield)
        self.basics.send_text_to_element(Selectors.username_passwordfield, "secret_sauce")
        self.basics.click_element(Selectors.login_button)

    def fill_in_address(self, first_name, last_name, postal_code):
        self.basics.send_text_to_element(Selectors.first_name, first_name)
        self.basics.send_text_to_element(Selectors.last_name, last_name)
        self.basics.send_text_to_element(Selectors.postal_code, postal_code)

    def test_buying_3_items(self):
        # login to web application
        self.log_in_with_standard_user_account()

        # change sort order from high to low price
        self.basics.click_element(Selectors.sort_price_high_to_low)

        # add any 3 products to the cart
        self.basics.click_element(Selectors.add_to_cart_item_1)
        self.basics.click_element(Selectors.add_to_cart_item_2)
        self.basics.click_element(Selectors.add_to_cart_item_3)

        # navigate to the shopping cart
        self.basics.click_element(Selectors.shopping_cart)

        # checkout your order
        self.basics.click_element(Selectors.checkout_order_button)

        # fill the data (first, last name and zip code)
        self.fill_in_address(first_name="Monika", last_name="Umyka", postal_code="11-100")

        # click continue
        self.basics.click_element(Selectors.continue_button)

        # calculate the tax value in the code
        total_price = self.basics.price(Selectors.summary_total)
        subtotal_price = self.basics.price(Selectors.summary_subtotal)
        tax_price = self.basics.price(Selectors.summary_tax)
        calculated_tax = float(total_price) - float(subtotal_price)

        # assertion that expected tax value from web is same as the calculated one
        self.assertAlmostEqual(float(tax_price), calculated_tax)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

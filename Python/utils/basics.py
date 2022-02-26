from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


class Basics:
    def __init__(self, driver):
        self.local_driver: webdriver.Chrome = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 5)

    def get_element_text(self, element):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        return self.local_driver.find_element(By.XPATH, element).text

    def clear_element(self, element):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        self.local_driver.find_element(By.XPATH, element).clear()

    def send_text_to_element(self, element, text):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        self.local_driver.find_element(By.XPATH, element).send_keys(text)

    def click_element(self, element):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        self.local_driver.find_element(By.XPATH, element).click()

    def price(self, element):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        numbers = re.findall("""\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})""", self.local_driver.find_element(By.XPATH, element).text)
        number, *_ = numbers
        return number

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

# This example requires Selenium WebDriver 3.13 or newer
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://google.com/ncr")
    driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
    first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3")))
    print(first_result.get_attribute("textContent"))

# A
# Add different numbers of 10 products from 2 different categories to the cart

# B
# Remove 1 product from the cart

# C
# Register new account

# D
# Choose payment on delivery

# E
# Choose 1 of 2 delivery services

# F
# Confirm order

# G
# Check order status

import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker

driver = webdriver.Chrome()
driver.implicitly_wait(10)
fake = Faker()

driver.get("https://www.saucedemo.com")

driver.maximize_window()

# Assert login functionality works
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Click the add to cart button on all products.
add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Add to cart')]")

for btn in add_to_cart_buttons:
 btn.click()

# Click the cart button to go to the cart page.
driver.find_element(By.ID, "shopping_cart_container").click()

time.sleep(2)

# remove the last item in the cart.
remove_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Remove')]")
if remove_buttons:
    remove_buttons[-1].click()

    time.sleep(3)

# checkout
driver.find_element(By.XPATH, "//button[@name='checkout']").click()

# driver.find_element(By.XPATH, "//input[value()").click()
driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys(fake.first_name())
driver.find_element(By.ID, "last-name").send_keys(fake.last_name())
driver.find_element(By.ID, "postal-code").send_keys(fake.postcode())
driver.find_element(By.ID, "continue").click()

driver.find_element(By.ID, "finish").click()

driver.find_element(By.ID, "back-to-products")

# Logout
driver.find_element(By.ID, "react-burger-menu-btn").click()
driver.find_element(By.ID, "logout_sidebar_link").click()

time.sleep(5)
driver.quit()
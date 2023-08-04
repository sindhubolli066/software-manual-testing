from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (Chrome in this example)
driver = webdriver.Chrome()

# Open the login page
driver.get("https://example.com/login")

# Find the username and password fields and enter credentials
username_field = driver.find_element_by_id("username")
password_field = driver.find_element_by_id("password")

username_field.send_keys("your_username")
password_field.send_keys("your_password")

# Find and click the login button
login_button = driver.find_element_by_id("loginButton")
login_button.click()

# Wait for a few seconds to observe the result (you might want to use explicit waits here)
time.sleep(3)

# Verify the expected outcome (this can be checking for a successful login or an error message)
if "Dashboard" in driver.title:
    print("Login successful!")
else:
    print("Login failed!")

# Close the browser
driver.quit()

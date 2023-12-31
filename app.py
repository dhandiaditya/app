import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def submit_coupon():
    # Define the URL of the webpage
    url = "https://www.real.discount/"

    # Set up the Chrome driver
    chrome_driver_path = "/chromedriver.exe/"  # Replace with the actual path to chromedriver executable
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=options)

    # Load the webpage
    driver.get(url)

    # Add a delay if necessary
    time.sleep(5)

    # Wait for the page to load
    wait = WebDriverWait(driver, 30)  # Increase the timeout value if needed
    wait.until(EC.visibility_of_element_located((By.ID, 'urls')))  # Use a different locator strategy if necessary

    # Find the text area for the coupon link and enter the link
    textarea = driver.find_element(By.ID, "urls")  # Use a different locator strategy if necessary
    final_url = "https://www.udemy.com/course/oops-with-python-object-oriented-programming-language/?couponCode=052836015188\nhttps://www.udemy.com/course/advanced-postgresql-for-professionals/?couponCode=051227445896"
    textarea.send_keys(final_url)

    # Submit the form
    submit_button = driver.find_element(By.NAME, 'submit1')
    submit_button.click()

    # Close the driver
    driver.quit()

if __name__ == '__main__':
    st.write('Click the button below to submit the coupon.')
    if st.button('Submit Coupon'):
        submit_coupon()
        st.write('Coupon submitted successfully!')

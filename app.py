
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import urllib.request
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def submit_coupon():
    # Define the URL of the webpage
    url = "https://www.real.discount/"
    
    # Set up the Chrome driver
    chrome_driver_path = "chromedriver.exe"  # Replace with the actual path to chromedriver executable
    service = Service(chrome_driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(service=service, options=options)
    
    # Load the webpage
    driver.get(url)

    
    # Wait for the page to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.NAME, 'urls')))
    
    # Find the text area for the coupon link and enter the link
    textarea = wait.until(EC.presence_of_element_located((By.NAME, "urls")))
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

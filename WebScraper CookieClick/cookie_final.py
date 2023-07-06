from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set the default Selenium driver path
# On macOS, select the file and hold the "Option" key, then click "Copy" from the "File" menu
# On Windows, right-click on the driver executable, select "Properties," and copy the "Location" field
chrome_driver_path = "/Users/stefanbaudoin/Documents/chromedriver_mac64/chromedriver"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

start = True

while True:
    try:
        continue_link = driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div[2]/p[2]/a')
        continue_link.click()
        time.sleep(0.5)  # Wait for a short duration before checking again
    except:
        # Check if redirected to the page with continue_link again
        redirected = driver.find_elements(By.XPATH, '//*[@id="wrap"]/div/div[2]/p[2]/a')
        if len(redirected) > 0:
            continue
        else:
            break

# Wait for the consent button to become clickable
wait = WebDriverWait(driver, 10)
consent_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="cc_btn cc_btn_accept_all"]')))
consent_button.click()

consent_button2 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]/p')
consent_button2.click()

# Now we are on the consent page, continue with the remaining code

language_button = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
language_button.click()

button = driver.find_element(by=By.ID, value="bigCookie")

start = True
wait_duration = 1100
wait_duration2 = 12000
wait_duration3 = 130000

while start:
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bigCookie"]')))
    button.click()
    wait_duration -= 1
    if wait_duration == 0:
        product2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product2"]')))
        product2.click()
        button.click()
        if wait_duration2 == 0:
            product3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id ="product3"]')))
            product3.click()
            button.click()
            if wait_duration3 == 0:
                product4 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product4"]')))
                product4.click()
                button.click()

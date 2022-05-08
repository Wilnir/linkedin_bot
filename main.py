import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.linkedin.com/login?fromSignIn=true&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs&trk="
           "guest_homepage-jobseeker_nav-header-signin")
user_id = driver.find_element(By.ID, "username")
user_id.send_keys("wilnir@hotmail.com")
password = driver.find_element(By.ID, "password")
password.send_keys("NOSSAdiarreia-138")
password.send_keys(Keys.ENTER)

time.sleep(20)
find_card = driver.find_element(By.CSS_SELECTOR, ".job-card-list__title")
find_card.click()

time.sleep(5)
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
        easy_apply.click()
        time.sleep(2)
        submit_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
        if submit_button.get_attribute("data-control-name") != "":
            close_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--secondary")
            discard_button.click()
            print("discarded")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, ".artdeco-button--tertiary")
        close_button.click()

    except NoSuchElementException:
        print("xubla")
        continue
time.sleep(2)
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys # This is useful too
# https://facebook.com/robots.txt - this shows all your automation access
# almost every website has this
# got his tip from - https://towardsdatascience.com/web-scraping-with-selenium-d7b6d8d3265a

timeout = 20

options = webdriver.ChromeOptions()
#options.add_argument(" — incognito")
# Use exact absolute location and paths
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
chrome_driver_binary = "C:\\Users\\linpa\\AppData\\Roaming\\JetBrains\\PyCharmCE2020.1\\scratches\\chromedriver.exe"

browser = webdriver.Chrome(chrome_driver_binary, options=options)
browser.get("http://facebook.com")

try:
    # What the fuck is this line - explore this nonsense - tutorial is fine - but we need docs
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div/div[1]/div/img")))
except TimeoutException:
    print("Timed out waiting for the page to load")
    browser.quit()

email_form = browser.find_elements_by_xpath("//*[@id='email']")
password_form = browser.find_elements_by_xpath("//*[@id='pass']")
email_form[0].send_keys("<enter_username_here>")
password_form[0].send_keys("<enter_password_here>")
password_form[0].send_keys(Keys.RETURN)


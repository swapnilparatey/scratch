# These Medium articles aren't 100% updated - and not well formatted - so be careful
# https://medium.com/the-andela-way/introduction-to-web-scraping-using-selenium-7ec377a8cf72
# https://github.com/TheDancerCodes/Selenium-Webscraping-Example/blob/master/webscraping_example.py
#
# Use cases of scraping:
# Contact Scraping
# Data Mining
# Online Price Change Monitoring & Price Comparison
# Product Review Scraping: to watch your competition
# Gathering Real Estate Listings
# Weather Data Monitoring
# Website Change Detection
# Research
# Tracking Online Presence and Reputation
# Web Data Integration
#
# I'm not happy with this because Brave and Chrome both use your private and personal data
# Both of the browsers and the Chrome webdriver send data to the websites saying it's being automated
# This is not what I want - I want super control - like the other end cannot tell - they're being run by automation

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

timeout = 20
count = 7
titles = []
languages = []

options = webdriver.ChromeOptions()
#options.add_argument(" — incognito")
# Use exact absolute location and paths
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
chrome_driver_binary = "C:\\Users\\linpa\\AppData\\Roaming\\JetBrains\\PyCharmCE2020.1\\scratches\\chromedriver.exe"

browser = webdriver.Chrome(chrome_driver_binary, options=options)
browser.get("https://github.com/TheDancerCodes")

try:
    # What the fuck is this line - explore this nonsense - tutorial is fine - but we need docs
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[4]/main/div[2]/div/div[1]/div/div[2]/div[1]/a/img")))
except TimeoutException:
    print("Timed out waiting for the page to load")
    browser.quit()

for i in range(1, count):
    xpath_name_project_title = "/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[1]/div/ol/li[ " + str(i) + "]/div/div/div/a/span"
    xpath_name_languages = "/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[1]/div/ol/li[" + str(i) +"]/div/div/p[2]/span/span[2]"
    project_titles_elements = browser.find_elements_by_xpath(xpath_name_project_title)
    language_elements = browser.find_elements_by_xpath(xpath_name_languages)
    titles.append([title.text for title in project_titles_elements])
    languages.append([language.text for language in language_elements])

print(titles)
print(languages)

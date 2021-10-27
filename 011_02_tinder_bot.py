from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import random


def create_browser():
    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    chrome_driver_binary = "C:\\Users\\linpa\\AppData\\Roaming\\JetBrains\\PyCharmCE2020.1\\scratches\\chromedriver.exe"
    browser = webdriver.Chrome(chrome_driver_binary, options=options)
    return browser


def login_tinder(browser):
    browser.get("http://tinder.com")
    # find the login button on the landing page
    login_btn = browser.find_elements_by_xpath('//*[@id="u-264510806"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
    login_btn[0].click() # click on the login button
    # choose the login by phone option
    sleep(2)
    login_by_phone = browser.find_elements_by_xpath('//*[@id="u-1992891882"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    login_by_phone[0].click()
    # Nasty verification process - have to do this manually
    # Then a few clicks here and there - with the splash screen and all - write code for this process
    try:
        WebDriverWait(browser, 20000).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="onboarding-description"]')))
    except TimeoutException:
        print("Timed out waiting for the page to load")
        browser.quit()
    sleep(2)
    allow_location = browser.find_elements_by_xpath('//*[@id="u-1992891882"]/div/div/div/div/div[3]/button[1]')
    allow_location[0].click()
    # fuck - forgot the other one - not interested for the location one
    sleep(2)
    no_notifications_for_matches = browser.find_elements_by_xpath('//*[@id="u-1992891882"]/div/div/div/div/div[3]/button[2]/span')
    no_notifications_for_matches[0].click()
    sleep(2)
    cookies_accept_yea_right = browser.find_elements_by_xpath('//*[@id="u-264510806"]/div/div[2]/div/div/div[1]/button/span')
    cookies_accept_yea_right[0].click()


def auto_swipe(browser):
    likes = 0
    dislikes = 1
    while True:
        like_to_dislike_ratio = likes / dislikes
        wait_time = random.randint(0, 800)
        sleep(wait_time / 100)
        try:
            if like_to_dislike_ratio < 0.73 and random.randint(0,100) > 30:
                like_btn = browser_window.find_elements_by_xpath('//*[@id="u-264510806"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
                like_btn[0].click()
                likes += 1
            else:
                dislike_btn = browser_window.find_elements_by_xpath('//*[@id="u-264510806"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')
                dislike_btn[0].click()
                dislikes += 1
        except Exception as e:
            print(e.args)
            try:
                no_thanks_super_like = browser_window.find_elements_by_xpath('//*[@id="u-264510806"]/div/div[1]/div/main/div[1]/div/div')
                no_thanks_super_like[0].click()
            except Exception as e:
                try:
                    # Write that MATCH code here
                    print("we matched immediately")
                except Exception as e:
                    print("whatever")


if __name__ == "__main__":
    browser_window = create_browser()
    login_tinder(browser_window)
    # auto_swipe(browser_window) - run this manually on the console and watch the swipes
# Trying out example for Mechanical Soup in later part of - https://realpython.com/python-web-scraping-practical-introduction/
# This is considered headless browsing - to fill up forms and shit - with a Browser object
# View source of a website - to check the CSS ID selectors - and then use #<id>

import mechanicalsoup
import time

browser = mechanicalsoup.Browser()                      # browser is a Browser object
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)                           # login_page is a Response object
login_html = login_page.soup                            # login_html is text


form = login_html.select("form")[0]                     # form is a Tag object
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = browser.submit(form, login_page.url)    # profiles_page is a Response object

print(profiles_page.url)
print(profiles_page.soup.title)

##########################################

# The string "#result" that you pass to .select() uses the CSS ID selector
# to indicate that result is an id value.

url = "http://olympus.realpython.org/dice"
dice_result_page = browser.get(url)
dice_result_html = dice_result_page.soup

# The [0] chooses the Tag object inside the ResultSet object (which is basically a list)
result = dice_result_html.select("#result")[0]  # Without the 0, you get a ResultSet object
print(result.text)

#############################################
# Another way to do the exact same program as above

browser = mechanicalsoup.Browser()
page = browser.get("http://olympus.realpython.org/dice")
tag = page.soup.select("#result")[0]
result = tag.text

print(f"The result of your dice roll is: {result}")

################################################

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")

    # Wait 10 seconds if this isn't the last request
    if i < 3:
        time.sleep(10)
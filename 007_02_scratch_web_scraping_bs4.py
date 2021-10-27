# BS4 implementation in https://realpython.com/python-web-scraping-practical-introduction/
# lxml is better for HTML parsing than BS4 - BS4 is an HTML parser that's all
# This is the hierarchy of awesomeness - lxml, bs4, re.search/regex, find

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# Instead of relying on find() and re.search regex expressions - you can use BS4 for extraction
print(html)
print(soup.get_text())          # Only the text part without the HTML
print(soup.find_all("img"))     # find_all() Returns Tag object
print(soup.find_all("img", src="/static/dionysus.jpg"))     # Can even mention the source

# You can get these two objects because you know this page is going to get you two objects
# Otherwise you're getting a list of all tag objects with img tags
image1, image2 = soup.find_all("img")
print(image1["src"])
print(image2["src"])

# Beautiful Soup HTML parser - with basic titles parsing
print("b: ",soup.title)
print("a: ",soup.title.string)

#########################################

url = "http://olympus.realpython.org/profiles"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

for link in soup.find_all("a"):
    link_url = url + link["href"]
    print(link_url)

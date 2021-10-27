# This is a FAIL - parsing Finviz for a tiny bit of information is harder than it looks
# Time to go parse some real websites and check for yourself how things work

import urllib.request
from bs4 import BeautifulSoup

# Add the ticker symbol as an addition/concatenation to the url string
url = "https://finviz.com/quote.ashx?t=BIOX"

# This header gave problems initially - had to change the Accept-Encoding to 'none'
hdr = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'none',
'X-Requested-With': 'XMLHttpRequest',
'Connection': 'keep-alive'
}

# Have no idea what I'm upto
request = urllib.request.Request(url,None,hdr)
response = urllib.request.urlopen(request)
html = response.read()
soup = BeautifulSoup(html, "html.parser")

# Learn how to organize output text - like strip CR, LF, NL characters - byte orders
# This is nonsensical - and learn how to put all the strings into a dict with key-valur
# Or learn how to stash individual strings into a list so you can pull the one you want
html_text = soup.get_text()


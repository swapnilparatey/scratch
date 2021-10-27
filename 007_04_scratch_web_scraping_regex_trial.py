# Basic regex explanation while on https://realpython.com/python-web-scraping-practical-introduction/
# Because not all websites have "<title>", some have "<title >", so you need regex
# [TODO] More details on Regexes -  https://realpython.com/regex-python/

import re
from urllib.request import urlopen

# First parameter is the pattern to tbe searched ab*c and second is the string to search the pattern in
# So it searches for a in the start, c in the end, and 0 or multiple instances of b in the middle (*)
print("Wildcard pattern search ab*c")
print(re.findall("ab*c", "ac"))
print(re.findall("ab*c", "abcd"))
print(re.findall("ab*c", "acc"))
print(re.findall("ab*c", "abcac"))
print(re.findall("ab*c", "abdc"))

print("Wildcard pattern search ab*c without and with IGNORECASE")
print(re.findall("ab*c", "ABC"))
print(re.findall("ab*c", "ABC", re.IGNORECASE))

# Now we work with period (.) - stands for single character in the pattern
print("Character period - find pattern with any one character in between")
print(re.findall("a.c", "abc"))
print(re.findall("a.c", "abbc"))
print(re.findall("a.c", "ac"))
print(re.findall("a.c", "acc"))

# .* - stands for any character repeated any number of times between a and c
print("Find pattern with any number of characters in between")
print(re.findall("a.*c", "abc"))
print(re.findall("a.*c", "abbc"))
print(re.findall("a.*c", "ac"))
print(re.findall("a.*c", "acc"))

# MarchObject returned by .search()
match_results = re.search("ab*c", "ABC", re.IGNORECASE)
print(match_results.group())

# replace text with re.sub()
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)
# This one is greedy - output is halved - second tags don't show
# It replaces <> beginning of replaces - and till the end of tags - greedy
print(string)

# replace text with re.sub() with non-greedy method
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
# This time it replaces matches on both <> tags - non-greedy
print(string)

########################################################################

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)

########################################################################
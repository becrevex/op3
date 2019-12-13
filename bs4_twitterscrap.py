#!/usr/bin/env python
# Filename: bs4_twitterscrap.py
# This program is optimized for Python 3.4
# Description: Kinda broken BeautifulSoup Twitter Scrapper
#   counterpart: None


from bs4 import BeautifulSoup as soupy
import urllib.request
import re
html = urllib.request.urlopen('https://twitter.com/ArianaWarfare?lang=en').read()
soup = soupy(html, features="html.parser")

x = soup.find_all("meta", {"name":"description"})['content']
d = soup.find_all("div")

filter = re.findall(r'"(.*)"', x) 
tweet = filter[0]  

print(tweet)

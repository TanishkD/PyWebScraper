import requests
from bs4 import BeautifulSoup

URL = 'http://ethans_fake_twitter_site.surge.sh/?ref=hackernoon.com'
page = requests.get(URL)

#print(page.text)
soup = BeautifulSoup(page.content, 'html.parser')

tweetcontainer = soup.find("div", class_="tweetcontainer")
horizDiv = tweetcontainer.find("div", class_="horizontalDivider")
vertDiv = horizDiv.find("div", class_="verticalDivider")
author = vertDiv.find("h2", class_="author")
print(author)

# Name: h2 class="author"
# Tweet: p class="content"
# Date: h5 class="dateTime"
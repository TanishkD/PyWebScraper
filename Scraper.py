import requests

URL = 'http://ethans_fake_twitter_site.surge.sh/?ref=hackernoon.com'
page = requests.get(URL)

print(page.text)
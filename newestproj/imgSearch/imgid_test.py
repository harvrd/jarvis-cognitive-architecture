import bs4
import requests

# if you're having problems with collections remove these 2 lines, this is to fix an issue with python versions in my env
import collections
collections.Callable = collections.abc.Callable


from bs4 import BeautifulSoup
import re

# unsuccessful attempt to not look like a bot to google :( 
# i might work on this more... but quite hard to get around web hidden path...
headers = {
    'Host': 'www.google.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.google.com/',
    'Origin': 'https://www.google.com',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'TE': 'Trailers'
}

# get rev imgsearch webpage
response = requests.get(
    "https://lens.google.com/search?ep=gisbubu&hl=en&re=df&p=ATHekxe2j6Ad_jYlpM-hxG_T1JKWDh3sLhIg_P_FN0TjEgd3QqztClWsoMY1zq47KdrfoxIqjhItnIGDgjUtYwPwkvUqjA2jd9Bb-3Yyz5TWOXtoSK5awdJbROzcdrN11XBVKn1QCaq0QqxaAPPVC_BgP7W8km1DU6M5ozpdQ551HxV7YAY9naprCkCs94vCYC01N2kgdcVl3BUQLKGRUqU6-CbavZsDEO0-DIyCzhCvsn6dpBayz4PNrqJZ4ESLthO2k6srYsN1BpElNYt1WUtq2z0guehXwVIF_u-Gt5rJxucmZAmTeUdN4n4K_vAB-cs%3D#lns=W251bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsIkVrY0tKREkwTnpkbE9UQXlMVGs1TkRrdE5HTm1ZUzFpWmpsbExUaGhaakV3TnpnNU5tTmxZeElmV1RRd2JYTXdOV1poUjBGWFJVWkRjWGQ0VEhKTVVEZHhNM2RHTTJsb1p3PT0iXQ==", timeout=10)

soup = BeautifulSoup(response.text, 'html.parser')

# this uses regex to find useful info on the page but this could be improved maybe...
matches = soup.body.find_all(string=re.compile("Search"))

# this uses regex again to isolate the object identification
result = re.search(r'Image search (.+?)"', str(matches))

if result:
    extracted_text = result.group(1)
    print(extracted_text)


# output: Apple MacBook Pro

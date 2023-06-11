# implementation of imgid_test.py with selenium 

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import collections

collections.Callable = collections.abc.Callable

from bs4 import BeautifulSoup

import codecs

import re

from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


val = "https://lens.google.com/search?ep=gisbubu&hl=en&re=df&p=ATHekxe2j6Ad_jYlpM-hxG_T1JKWDh3sLhIg_P_FN0TjEgd3QqztClWsoMY1zq47KdrfoxIqjhItnIGDgjUtYwPwkvUqjA2jd9Bb-3Yyz5TWOXtoSK5awdJbROzcdrN11XBVKn1QCaq0QqxaAPPVC_BgP7W8km1DU6M5ozpdQ551HxV7YAY9naprCkCs94vCYC01N2kgdcVl3BUQLKGRUqU6-CbavZsDEO0-DIyCzhCvsn6dpBayz4PNrqJZ4ESLthO2k6srYsN1BpElNYt1WUtq2z0guehXwVIF_u-Gt5rJxucmZAmTeUdN4n4K_vAB-cs%3D#lns=W251bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsIkVrY0tKREkwTnpkbE9UQXlMVGs1TkRrdE5HTm1ZUzFpWmpsbExUaGhaakV3TnpnNU5tTmxZeElmV1RRd2JYTXdOV1poUjBGWFJVWkRjWGQ0VEhKTVVEZHhNM2RHTTJsb1p3PT0iXQ=="

wait = WebDriverWait(driver, 30)

driver.get(val)


get_url = driver.current_url
wait.until(EC.url_to_be(val))


if get_url == val:

    page_source = driver.page_source

soup = BeautifulSoup(page_source, features="html.parser")
matches = soup.body.find_all(string=re.compile("Search"))

result = re.search(r'Image search (.+?)"', str(matches))

if result:
    extracted_text = result.group(1)
    print(extracted_text)

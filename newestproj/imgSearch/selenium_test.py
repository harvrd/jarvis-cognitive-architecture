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


val = "https://lens.google.com/search?ep=gisbubu&hl=en&re=df&p=ATHekxe6PIKMujk8K_8RtNEv9ICVT94JOE-S_QNihHf4erie4yyH7hVovIt9KpOB8o9pmmENuTADud5Yrl5yNGJ93SC5praT5jsDIygq6MnvdHl9a90xgtQ2aFhqZIzZDlfmbrj4c8k1QxGR7OBS4BPPmNp7qPEEYbNJSGb-8RYm_Ro9Ql3QbUUEjLtprPQQeuElpeKDupyHmNqOA09jRqqSn5Xg9syBbYH7ftW8wKF-C5-nq4YeWw-9mWOH2EhNHmlMj9Th1Kh_PzEKm_TybaLHlK3-wPgoAsn23YtWLUwXboO_sEAzAQbr4L-ZfFP67p0%3D#lns=W251bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsIkVrY0tKREkxTURRMk5tSXlMVFJoTm1JdE5EVmxOUzA0WVRkaUxURXlabU15TlRoall6UXpaUklmYjNsM1RWcGlNVEEzY1hOYVJVWkRjWGQ0VEhKTVVEUmhjVkI1ZW1sb1p3PT0iXQ=="

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

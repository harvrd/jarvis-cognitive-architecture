from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20)
driver.get("https://images.google.com/")

# click the lens icon
lens_path = 'div[data-ved][aria-label="Search by image"]'
lens = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, lens_path))
)
lens.click()

# now the img search menu is open
# search by img url
url_search_path = 'input'
url_search = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, url_search_path))
)
url_search.send_keys("https://i.imgur.com/TVSIyzx.jpg")

# click the search button
search_button_path = '//div[text()="Search"]'
search_button = wait.until(
    EC.presence_of_element_located((By.XPATH, search_button_path))
)
search_button.click()

# now we're on the rev img search page
results_page = driver.page_source

# now we webscrape
soup = BeautifulSoup(results_page, features="html.parser")
matches = soup.body.find_all(string=re.compile("Search"))

result = re.search(r'Image search (.+?)"', str(matches))

if result:
    extracted_text = result.group(1)
    print(extracted_text)

time.sleep(5)
driver.quit()

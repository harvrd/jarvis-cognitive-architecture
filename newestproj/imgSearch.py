from serpapi import GoogleSearch
from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException
from urllib3.exceptions import MaxRetryError
import key

newkey = key.key()

def imgSearch(img_url):
    params = {
        "engine": "google_reverse_image",
        "image_url": img_url,
        "api_key": newkey,
        "gl": "us",
        "hl": "en",
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    image_results = results["image_results"]
    sources = [image["link"] for image in image_results]

    max_retries = 3

    # web scraping
    soups = "Everything in <title> is information about this image: \n"

    for source in sources:
        retries = 0
        while retries < max_retries:
            try:
                response = requests.get(source, timeout=10)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')
                soups += str(soup.title) + "\n"
                break
            except (RequestException, MaxRetryError) as e: 
                retries += 1
                if retries == max_retries:
                    print(f"Max retries exceeded for {source}. Skipping...")
                    break
                print(f"An error occurred while processing {source}: {e}")

    return soups

# write webscrape results
# with open("soups.txt", "w") as f:
#     f.write(soups)

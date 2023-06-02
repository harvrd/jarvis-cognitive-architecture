import bs4
import requests
import collections
collections.Callable = collections.abc.Callable


from bs4 import BeautifulSoup

def request():
    response = requests.get(
        "https://lens.google.com/search?p=ATHekxcGLvnh9XbXAnpRRxAPCNAK_eJFt4x-KCBUb3y9tsgIrhZRKYZJzmC6hivZ6ddezy4Y25kARr0oTO19mPWDODz5ixnYvNfYoQ1pbdk_mTPEdREMic2i7g5tB9Ctup6ihAuEmr7HzEpofDdxK2qiSNeNQCXYGE1vzh6afg0wyJxUhLiLjzhmSle-JBaptKsWFGkwZL_KAViMM9ixSkd4vwFiglZFbhT33c8ICNeLSvElGVZkxNC-w3tGprPMwp5mMGGcW-ZRBZE7t6yPq8R-B0aYOvyBl1jnkyzldIYTPzcfXLU%3D&ep=gisbubu&hl=en&re=df#lns=W251bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsIkVrY0tKR0kzTUdVek5HSXhMVEpsWkRrdE5HSmxOUzA1WTJJM0xUazBOekExTVdFNU9EY3daaElmT0RkUVFqRmxaRlpzU1hkV2MwRmhRM1F0VldoaFp6VlBRWFZwWW1oNFp3PT0iXQ==", timeout=10)

    soup = BeautifulSoup(response.text, 'html.parser')

    with open("soup.html", 'w') as file:
        file.write(str(soup))

    element = soup.find_all(class_='DeMn2d')

    print(element)

request()

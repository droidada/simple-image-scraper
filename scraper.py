import requests
from bs4 import BeautifulSoup

def match_substring_recursive(needle, haystack):
    if isinstance(haystack, str):
        return needle in haystack
    else:
        return any(match_substring_recursive(needle, x) for x in haystack)

def scrape(img_name, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    images = soup.select('img')

    for i, j in enumerate(images):
        if match_substring_recursive(img_name, j):
            print(i)
        else:
            print('image name not found')


if __name__ == '__main__':
    img_name = input()
    url = input()
    scrape(img_name, url)

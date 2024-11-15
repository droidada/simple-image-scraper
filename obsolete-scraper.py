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

    for item in soup.find_all('img'):
        #print(item['src'])
        if img_name == item['alt']:
            print('found')


if __name__ == '__main__':
    img_name = input()
    url = input()
    scrape(img_name, url)

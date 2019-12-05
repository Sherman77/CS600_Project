from bs4 import BeautifulSoup
import requests

punctuation = ''.join([".", ",", "/", "==", "//", "<", ">", "?", ";", "'", ":",
            "\“", "[", "]", "\\", "{", "}", "|", "+", "-", "=", "!", "@", "#", "$", "%", "^", "&", "*", "(",
            ")", "_", "-", "\”", "\"", "—"])

translator = str.maketrans('', '', ''.join(punctuation))

def get_links(url, limit):
    """Get all the links from a url"""
    try:
        page = requests.get(url=url, timeout=10)
    except requests.exceptions.RequestException as e:
        print(e)
    else:
        count = 0
        soup = BeautifulSoup(page.content, "lxml").find_all('a', href=True)
        links = []
        for i in soup:
            if count == limit:
                return links
            elif i['href'].startswith('http'):
                links.append(i['href'])
                count += 1
        return links

def get_words(url):
    """Get all the words from a html text"""
    page = requests.get(url=url).content
    soup = BeautifulSoup(page, "lxml").find_all('p')
    #translator = str.maketrans('', '', ''.join(punctuation))
    words = ''
    for i in soup:
        words += i.text
    for word in words.translate(translator).split(' '):
        yield word




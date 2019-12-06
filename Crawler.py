from bs4 import BeautifulSoup
import requests

punctuation = ''.join([".", ",", "/", "==", "//", "<", ">", "?", ";", "'", ":",
            "\“", "[", "]", "\\", "{", "}", "|", "+", "-", "=", "!", "@", "#", "$", "%", "^", "&", "*", "(",
            ")", "_", "-", "\”", "\"", "—"])

stop_words = ["the", "a", "an", "i", "you", "he", "she", "it", "they", "we", "me", "him",
            "her", "them", "us", "aboard", "about", "above", "across", "after", "afterwards", "against", "again", "all", "along", "among", "amongst","around",
            "as", "at", "already", "also", "and", "amount", "another", "any", "anyone", "anywhere", "anything", "anyone", "anyhow",
            "always", "because", "become", "been", "below", "being", "before", "behind", "below", "beside", "besides",
            "between", "bill","beyond", "but", "by", "both", "bottom","can", "cannot", "computer", "could", "despite",
            "detail", "due", "do", "describe", "down", "during", "each", "either", "ever", "every", "everyone", "everything",
            "everywhere", "even", "except", "following", "few", "former", "first", "found", "further", "for", "from", "had",
            "have", "here", "how", "hence", "however", "hundred", "has", "in", "inside", "into", "near", "of", "on", "onto",
            "over", "past", "since", "than", "to", "through", "toward", "towards", "under", "until", "up", "upon",
            "via", "with", "within", "without"]

translator = str.maketrans('', '', ''.join(punctuation))

def get_links(url, links, limit):
    """Get all the links from a url"""
    try:
        page = requests.get(url=url, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Can't fatch anything useful from {url}")
    else:
        print(f"Fatching links from {url}")
        count = 1
        soup = BeautifulSoup(page.content, "lxml").find_all('a', href=True)
        for i in soup:
            if count == limit:
                return links
            elif i['href'].startswith('http') and not i['href'] in links:
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
        if word in stop_words:
            continue
        else:
            yield word

def valid_url(url):
    r_code = requests.get(url=url)
    if r_code == 200:
        return True
    return False


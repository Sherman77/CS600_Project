from bs4 import BeautifulSoup
import requests
import re
import Trie
import string

punctuation = [".", ",", "/", "==", "//", "<", ">", "?", ";", "'", ":",
            "\“", "[", "]", "\\", "{", "}", "|", "+", "-", "=", "!", "@", "#", "$", "%", "^", "&", "*", "(",
            ")", "_", "-", "\”", "\"", "—"]

url = "https://www.nytimes.com/"

try:
    page = requests.get(url=url, timeout=10)

except requests.exceptions.RequestException as e:
    print(e)

else:

    soup = BeautifulSoup(page.content, "lxml").find_all('p')
    new = Trie.TrieNode()
    links = []
    translator = str.maketrans('', '', ''.join(punctuation))
    for i in soup:
        links.append(i.text)
    print(links)
#    for i in soup:
#        print(i.text)
'''    words = soup[9].text.split(' ')
    print(soup[9].text)
    for word in words:
        if word.translate(translator):
            print(word.translate(translator))'''
#print(soup[0].text.translate(str.maketrans('', '', string.punctuation)))

'''for wrd in str_lis:
    if wrd in checked:
        continue
    Trie.insert(new, wrd, url)
    checked.append(wrd)
    print(wrd)

print(Trie.search(new, 'Arts'))'''





""" def cleantag(string):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', string)
    return cleantext

for i in range(3):
    print(type(soup[i]))
    print('/n') """
from bs4 import BeautifulSoup
import requests
import re
import Trie

url = "http://www.numerix.com"

page = requests.get(url=url).text

soup = BeautifulSoup(page, "lxml").find_all('p')

new = Trie.TrieNode('#')

str_lis = []

for i in range(3):
    str_lis += soup[i].text.split(' ')

for wrd in str_lis:
    Trie.insert(new, wrd, url)

print(Trie.search(new, 'email'))





""" def cleantag(string):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', string)
    return cleantext

for i in range(3):
    print(type(soup[i]))
    print('/n') """
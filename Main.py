import Crawler
import Trie

punctuation = ''.join([".", ",", "/", "==", "//", "<", ">", "?", ";", "'", ":",
            "\“", "[", "]", "\\", "{", "}", "|", "+", "-", "=", "!", "@", "#", "$", "%", "^", "&", "*", "(",
            ")", "_", "-", "\”", "\"", "—"])

#trasnlator = 
root = Trie.TrieNode('#')
url = input("Please enter a website:")
limit = int(input("Please enter crawler limit:"))
links = [url]
links += Crawler.get_links(url, limit)
for link in links:
    checked = []
    text = Crawler.get_words(link)
    for i in text:
        if i and not i.lower() in checked:
            Trie.insert(root, i.lower(), link)
            checked.append(i.lower())

print(Trie.search(root, 'stevens'))


import Crawler
import Trie
from validator_collection import checkers
import requests

def get_url():
    """Get url from user's input"""
    entry = input("Please enter a URL for websit(e.g www.stevens.edu): ")
    if entry == 'EXIT':
        return 'EXIT'
    url = f"https://{entry}"
    if checkers.is_url(url):
        return url
    return False

def valid_url(url):
    """Check if we can get proper response from URL"""
    try:
        response = requests.get(url=url)
    except:
        return False
    else:
        if response.status_code == 200:
            return True
        return False

def get_num():
    """Get a limit crawler number from user"""
    entry = input("Please enter a integer for how many webpages you want to search: ")
    try:
        num = int(entry)
    except:
        return False
    else:
        if num > 0:
            return num
        return False

def get_search_word():
    """Get target word from user"""
    entry = input("Please enter the word you want to search, enter EXIT to end: ")
    return entry


def main():

    target = ''
    limit = 0
    switch = True
    links = []
    while switch == True:
        url = get_url()
        if url == 'EXIT':
            break
        if not url:
            print("The URL you entered is invalid!")
            continue
        if not valid_url(url):
            print("The URL you entered is invalid!")
            continue
        links.append(url)
        target = url
        break
    print("Got it!")

    while switch == True:
        num = get_num()
        if not num:
            print("Please enter a POSITIVE INTEGER!")
            continue
        limit = num
        break

    links = Crawler.get_links(target, links, limit)
    if len(links) < limit:
        print(f"We've fatch as many links as we can from the URL you entered, total is {len(links)}")
    
    root = Trie.TrieNode('#')
    
    for link in links:
        checked = []
        text = Crawler.get_words(link)
        print(f"Parsing {link}\n")
        for i in text:
            word = i.lower()
            if word and not word in checked:
                Trie.insert(root, word, link)
                checked.append(word)
    
    while switch == True:
        words = get_search_word()
        if words == 'EXIT':
            print("Thanks for using my search engine!")
            break
        result = Trie.search(root, words)
        if not result:
            print("Sorry, we couldn't find anything\n")
        else:
            try:
                answer = set(result[0]).intersection(*result)
            except:
                print(f"Target has been found at: {result[0]}\n")
            else:
                print(f"Target has been found at: {answer}\n")



if __name__ == '__main__':
    main()



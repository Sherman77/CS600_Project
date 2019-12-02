

class TrieNode:

    def __init__(self, char):

        self.char = char
        self.children = {}
        self.urls = []
        self.word_finished = False

def insert(root, word, url):
    """Insert a word into Trie and store its url"""
    node = root
    for char in word:
        if char in node.children:
            node = node.children[char]
        else:
            new_node = TrieNode(char)
            node.children[char] = new_node
            node = new_node
    if node.word_finished == False:
        node.word_finished = True
    node.urls.append(url)


def find(root, word):
    


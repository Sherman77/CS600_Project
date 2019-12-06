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

class TrieNode:

    def __init__(self, char=None):

        self.char = char
        self.children = {}
        self.urls = []
        self.word_finished = False

def insert(root, word, url):
    """Insert a word into Trie and store its url"""
    node = root
    if word in stop_words:
        return
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


def search(root, words):
    """Look for the word in Trie, return stored urls if found"""
    node = root
    result = []
    for word in words.split(' '):
        if word.lower() in stop_words:
            continue
        for char in word.lower():
            if char in node.children:
                node = node.children[char]
            else:
                break
        if node.word_finished == True:
            result.append(node.urls)
    return result

Search Engine -- Final project for CS600

# This is a Java implementation of search engine using trie and a simple crawler. 

I used a simple implementation of trie using HashSet. I used jsoup.jar to extract the words from the HTML pages. The stop words, punctuations and html identifiers are already written in th code.

Wiith each node (not null) of the trie, it refers to a specfic word. I marked all the urls corresponding to this word so that we can do a search after we constructed the trie.

# You need to import jsoup.jar to the project to work.

# Following the directions, you have to enter the vaild url you want to crawl. Then you need to type words that you want to search. Type exit to finish.
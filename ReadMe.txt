Xiaomeng Xu_Project_CS600

This is a Python implementation for a tiny search engine.
When using this search engine, user will enter a URL for target website, and an integer indicates how many links user want to search.
Crawler will automatically fatch all the hyperlinks on that tarhet website.
Once Craler fatch all the available links or reach the limitation for fatching links, this engine will parse each link and store all the words on that link into a Trie
User then enter a string indicates the words he want to search for. Search engine will return the url in which target string is presented.

Carwler is implemented with request and Beautifulsoup4

Please install validator_collection, Beautifulsoup4, request on your machine before using this engine.


import java.util.HashSet;
import java.util.Set;

/**
 * Created by apple on 2019/5/7.
 */
public class SearchEngine {
    public static Trie trie = new Trie('#');
    public static String[] stopWords = { "the", "a", "an", "i", "you", "he", "she", "it", "they", "we", "me", "him",
            "her", "them", "us", "aboard", "about", "above", "across", "after", "afterwards", "against", "again", "all", "along", "among", "amongst","around",
            "as", "at", "already", "also", "and", "amount", "another", "any", "anyone", "anywhere", "anything", "anyone", "anyhow",
            "always", "because", "become", "been", "below", "being", "before", "behind", "below", "beside", "besides",
            "between", "bill","beyond", "but", "by", "both", "bottom","can", "cannot", "computer", "could", "despite",
            "detail", "due", "do", "describe", "down", "during", "each", "either", "ever", "every", "everyone", "everything",
            "everywhere", "even", "except", "following", "few", "former", "first", "found", "further", "for", "from", "had",
            "have", "here", "how", "hence", "however", "hundred", "has", "in", "inside", "into", "near", "of", "on", "onto",
            "over", "past", "since", "than", "to", "through", "toward", "towards", "under", "until", "up", "upon",
            "via", "with", "within", "without" };

    public static String[] htmlIdentifier = { "a", "href", "p", "div", "img", "src", "html", "http", "body", "span", "class",
            "id", "name", "target", "style", "figure", "border", "width", "height" };

    public static String[] punctuation = { ".", ",", "/", "==", "//", "<", ">", "?", ";", "'", ":",
            "\"", "[", "]", "\\", "/{", "}", "|", "+", "-", "=", "!", "@", "#", "$", "%", "^", "&", "*", "(",
            ")", "_"};

    //method for search all urls that contains the query
    public static Set<String> searchWords(String target) {
        String[] words = target.split(" ");
        Set<String> result = new HashSet<>();
        for (String word : words) {
            Set<String> single = searchWord(word);
            if (single != null)
                result.addAll(single);
        }
        return result;
    }

    //determine whether a word is a stop word
    public static boolean isStopWord(String w) {
        String word = w.toLowerCase();
        for (String str : punctuation) {
            if (word.equals(str))
                return true;
        }
        for (String str : stopWords) {
            if (word.equals(str))
                return true;
        }
        for (String str : htmlIdentifier ) {
            if (word.equals(str))
                return true;
        }
        return false;
    }

    //If each word in the text of HTML page exists and is not a stop word,
    //we mark this url that contains this word
    public void markedUrl(String text, String url) {
        String[] words = text.split(" ");
        for (String word : words) {
            if (word.trim().length() > 0 && !isStopWord(word)) {
                insertWord(word.trim(), url);
            }
        }
    }

    //insert the word to the Trie
    private void insertWord(String target, String url) {
        Trie root = trie;
        String word = target.toLowerCase();
        for (int i = 0; i < word.length(); i++) {
            root.addChild(word.charAt(i));
            root = root.getChild(word.charAt(i));
        }
        root.addUrls(url);
    }

    public static Set<String> searchWord(String target) {
        System.out.println("Searching for \"" + target + "\"...");
        char[] words = target.toCharArray();
        Trie root = SearchEngine.trie;
        for (int i = 0; i < words.length; i++) {
            root = root.getChild(words[i]);
            if (root == null)
                return null;
        }
        return root.urls;
    }
}
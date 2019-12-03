/**
 * Created by apple on 2019/5/7.
 */
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Trie {
    public List<Trie> children;
    public char val;
    public Set<String> urls;
    public Trie(char v) {
        children = null;
        urls = null;
        this.val = v;
    }

    public void addUrls(String url) {
        if (urls == null) urls = new HashSet<>();
        if (!urls.contains(url)) urls.add(url);
    }

    //set method
    public void addChild(char c) {
        if (children == null) {
            children = new ArrayList<>();
        }
        if (!hasChild(c)) {
            children.add(new Trie(c));
        }
    }

    //check
    public boolean hasChild(char c) {
        if (children == null) return false;
        for (Trie trie : children) {
            if (trie.val == c) {
                return true;
            }
        }
        return false;
    }

    //get method
    public Trie getChild(char c) {
        if (children == null) return null;
        for (Trie trie : children) {
            if (trie.val == c) {
                return trie;
            }
        }
        return null;
    }
}

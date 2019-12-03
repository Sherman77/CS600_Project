/**
 * Created by apple on 2019/5/7.
 */
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.io.IOException;

import org.jsoup.Connection;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class Crawler {
    private int pagesToCrawl;
    private Set<String> visitedList = new HashSet<String>();
    private List<String> pageList = new LinkedList<>();

    private static final String USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112	Safari/535.1";
    private List<String> links = new LinkedList<String>();

    public Crawler(int pagesToCrawl) {
        this.pagesToCrawl = pagesToCrawl;
    }

    public void startCrawling(String url) {
        while(this.visitedList.size()< pagesToCrawl){
            String currentUrl;

            if(this.pageList.isEmpty()){
                currentUrl = url;
                this.visitedList.add(url);
            }
            else{
                currentUrl = this.nextUrl();
            }
            System.out.println("Visiting: "+currentUrl);
            crawl(currentUrl);

            this.pageList.addAll(getLinks());
        }
    }

    private String nextUrl(){
        String nextURL;
        do{
            nextURL = this.pageList.remove(0);
        }while(this.visitedList.contains(nextURL));
        this.visitedList.add(nextURL);

        return nextURL;
    }

    public void crawl(String Url) {
        try {
            System.setProperty("http.proxyHost", "nybcproxy3.mlp.com");
            System.setProperty("http.proxyPort", "3128");
            System.setProperty("https.proxyHost", "nybcproxy3.mlp.com");
            System.setProperty("https.proxyPort", "3128");

            Connection connection = Jsoup.connect(Url).userAgent(USER_AGENT);
            Document htmlDocument = connection.get();

            String text = htmlDocument.text();
            SearchEngine p = new SearchEngine();
            p.markedUrl(text, Url);

            Elements links = htmlDocument.select("a[href]");
            for (Element link : links) {
                this.links.add(link.absUrl("href"));
            }
        } catch (IOException ioe) {
            System.out.println("Error in HTTP request " + ioe);
        }
    }

    public List<String> getLinks() {
        return this.links;
    }
}
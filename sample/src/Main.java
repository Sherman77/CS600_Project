/**
 * Created by apple on 2019/5/7.
 */
import java.net.URL;
import java.util.Iterator;
import java.util.Scanner;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        String example = "https://www.reddit.com";
        int numOfPages;
        String url, pages;
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Please type a valid url or use the default url to start crawling:  Example: [" + example + "]:");
            url = scanner.nextLine();
            if (url.trim().length() > 0) {
                // validate the entered URL
                try {
                    URL u = new URL(url); // check for the protocol
                    u.toURI(); // does the extra checking required for validation of URL
                }   catch (Exception e) {
                    System.out.println("Please provide a valid url");
                    continue;
                }
            }
            else {
                url = example;
            }
            System.out.println("Please enter the number of pages to crawl:");
            pages = scanner.nextLine();
            try {
                // validate the entered number
                numOfPages = Integer.parseInt(pages);
                if (numOfPages < 1) {
                    throw new Exception();
                }
            } catch (Exception e) {
                System.out.println("Please provide a valid integer");
                continue;
            }

            //crawling
            Crawler crawler = new Crawler(numOfPages);
            crawler.startCrawling(url);
            break;
        }

        String target = "";
        while (true) {
            System.out.println("\nEnter a search query:  \nEnter exit to exit the program");
            target = scanner.nextLine();
            if (target.equals("exit")) {
                break;
            }
            if (SearchEngine.isStopWord(target)){
                System.out.println("\nThis is a stop word. Please enter an another query:");
                continue;
            }
            Set<String> urls = SearchEngine.searchWords(target);
            if (urls.size() == 0) {
                System.out.println("No results found!");
            }
            else {
                Iterator<String> iterator = urls.iterator();
                System.out.println(urls.size()+" Results Found: ");
                while (iterator.hasNext()) {
                    System.out.println(iterator.next());
                }
                System.out.print("\n");
            }
        }
        scanner.close();
    }
}

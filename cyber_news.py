import feedparser
import webbrowser
import sys

def news():
    print("--=Cybersecurity News=--")
    print("1) Threatpost")
    print("2) The Hacker News")
    print("3) Security Week\n")
    user_site = input("Which site would you like news from? Press 1-3 Or press 0 to exit ")
    print()

    try:
        int(user_site)
        if user_site == "0":
            print("Goodbye. Have an excellent day! ")
            sys.exit()
        elif user_site == "1":
            website = "https://threatpost.com/feed/"
            return website
        elif user_site == "2":
            website = "https://feeds.feedburner.com/TheHackersNews"
            return website
        elif user_site == "3":
            website = "https://feeds.feedburner.com/securityweek"
            return website
    except:
        sys.exit()

def cybersite(site):
    news_feed = feedparser.parse(site)
    print(f"Here is the latest news from {news_feed.feed.title.upper()}")
    article_link = []
    for i in range(10):
        article = news_feed.entries[i]
        titles = article.title
        link = article.link
        article_link.append(link)
        print(f"{i+1}) {titles}")
    print()
    article_link_click = False
    while not article_link_click:
        user_link = int(input("Which link would you like to view? Press 1-10 or 0 to exit "))
        print(user_link)
        if user_link == 0:
            print("Goodbye. Have an excellent day! ")
            break
        elif user_link >= 1 and user_link <= 10:
            int(user_link)
            webbrowser.open(article_link[user_link-1])
            article_link_click = True
        else:
            print("Invalid input1!\n")

cybersite(news())

import random
import feedparser

from lib.article import Article


def get_random_article(urls):
    feed_url = random.choice(urls)
    feed = feedparser.parse(feed_url)
    entries = feed.entries
    if entries:
        random_entry = random.choice(entries)
        return Article(random_entry)
    else:
        return None


def get_feed_title(url):
    return feedparser.parse(url).feed.title
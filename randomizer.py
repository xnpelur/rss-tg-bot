import random
import feedparser


def get_random_article(urls):
    feed_url = random.choice(urls)
    feed = feedparser.parse(feed_url)
    entries = feed.entries
    if entries:
        random_entry = random.choice(entries)
        return {
            'title': random_entry.title,
            'description': random_entry.description,
            'link': random_entry.link,
            'author': random_entry.author,
            'published': random_entry.published
        }
    else:
        return None
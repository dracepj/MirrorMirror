import feedparser

class RssFeed:
	news_entries = {}
	def __init__(self, rss_feeds):
		for url in rss_feeds:
			print("Parsing url %s", url["FeedUrl"])
			news = feedparser.parse(url["FeedUrl"])
			feed_entries = []
			for entry in range(0, len(news.entries)):
				print(news.entries[entry])
				feed_entries.append({ 'title': news.entries[entry].title, 'author': news.entries[entry].author })
			self.news_entries[news.feed.title] = feed_entries
			

